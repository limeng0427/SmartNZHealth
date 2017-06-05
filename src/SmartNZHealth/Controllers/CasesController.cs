using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.EntityFrameworkCore;
using SmartNZHealth.Data;
using SmartNZHealth.Models;
using SmartNZHealth.Models.CaseViewModels;

namespace SmartNZHealth.Controllers
{
    public class CasesController : Controller
    {
        private readonly ApplicationDbContext _context;
        private readonly UserManager<ApplicationUser> _userManager;
        private readonly SignInManager<ApplicationUser> _signInManager;

        public CasesController(
            UserManager<ApplicationUser> userManager,
            SignInManager<ApplicationUser> signInManager,
            ApplicationDbContext context)
        {
            _userManager = userManager;
            _signInManager = signInManager;
            _context = context;    
        }

        // GET: Cases
        public async Task<IActionResult> Index()
        {
            return View(await _context.Cases.ToListAsync());
        }

        // GET: Cases/Details/5
        [Authorize(Roles = "Doctor, Patient")]
        public IActionResult Details(string id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var user = _context.Users.Where(u => u.Id == id).Include(u => u.Cases).AsNoTracking().Single();
            if (user == null)
            {
                return NotFound();
            }

            List<ApplicationUser> doctors = new List<ApplicationUser>();
            foreach (var _case in user.Cases)
            {
                var doctor = _context.Users.Where(u => u.Id == _case.DoctorId).AsNoTracking().Single();
                doctors.Add(doctor);
            }
            ViewBag.Doctors = doctors;

            return View(user);
        }

        // GET: Cases/Create
        public IActionResult Create(string id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var user = _context.Users.Where(u => u.Id == id).Include(u => u.Cases).AsNoTracking().Single();
            if (user == null)
            {
                return NotFound();
            }

            //List<ApplicationUser> doctors = new List<ApplicationUser>();
            //foreach (var _case in user.Cases)
            //{
            //    var doctor = _context.Users.Where(u => u.Id == _case.DoctorId).AsNoTracking().Single();
            //    doctors.Add(doctor);
            //}

            ViewBag.User = user;
            //ViewBag.Doctors = doctors;
            //CreateViewModel temp = new CreateViewModel {
            //    User = user
            //};

            return View();
        }

        // POST: Cases/Create
        // To protect from overposting attacks, please enable the specific properties you want to bind to, for 
        // more details see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create([Bind("ConsultationDate, CaseDescription, Prescription")] Case @case, string Id, string DoctorId)
        {
            if (Id == null)
            {
                return NotFound();
            }

            var user = _context.Users.Where(u => u.Id == Id).Single();
            if (user == null)
            {
                return NotFound();
            }

            if (ModelState.IsValid)
            {
                @case.PatientId = Id;
                @case.Patient = user;
                @case.DoctorId = DoctorId;
                _context.Add(@case);
                await _context.SaveChangesAsync();
                return RedirectToAction("Details", new { id = user.Id });
            }
            return View(@case);
        }

        // GET: Cases/Edit/5
        public async Task<IActionResult> Edit(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var @case = await _context.Cases.SingleOrDefaultAsync(m => m.CaseID == id);
            if (@case == null)
            {
                return NotFound();
            }
            return View(@case);
        }

        // POST: Cases/Edit/5
        // To protect from overposting attacks, please enable the specific properties you want to bind to, for 
        // more details see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit(int id, [Bind("CaseID,CaseDescription,Prescription")] Case @case)
        {
            if (id != @case.CaseID)
            {
                return NotFound();
            }

            if (ModelState.IsValid)
            {
                try
                {
                    _context.Update(@case);
                    await _context.SaveChangesAsync();
                }
                catch (DbUpdateConcurrencyException)
                {
                    if (!CaseExists(@case.CaseID))
                    {
                        return NotFound();
                    }
                    else
                    {
                        throw;
                    }
                }
                return RedirectToAction("Index");
            }
            return View(@case);
        }

        // GET: Cases/Delete/5
        public async Task<IActionResult> Delete(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var @case = await _context.Cases.SingleOrDefaultAsync(m => m.CaseID == id);
            if (@case == null)
            {
                return NotFound();
            }

            return View(@case);
        }

        // POST: Cases/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> DeleteConfirmed(int id)
        {
            var @case = await _context.Cases.SingleOrDefaultAsync(m => m.CaseID == id);
            _context.Cases.Remove(@case);
            await _context.SaveChangesAsync();
            return RedirectToAction("Index");
        }

        private bool CaseExists(int id)
        {
            return _context.Cases.Any(e => e.CaseID == id);
        }
    }
}
