using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.EntityFrameworkCore;
using SmartNZHealth.Data;
using SmartNZHealth.Models;

namespace SmartNZHealth.Controllers
{
    public class PatientRecordsController : Controller
    {
        private readonly HealthContext _context;

        public PatientRecordsController(HealthContext context)
        {
            _context = context;    
        }

        // GET: PatientRecords
        public async Task<IActionResult> Index()
        {
            var healthContext = _context.PatientRecords.Include(p => p.Case).Include(p => p.Patient);
            return View(await healthContext.ToListAsync());
        }

        // GET: PatientRecords/Details/5
        public async Task<IActionResult> Details(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var patientRecord = await _context.PatientRecords.SingleOrDefaultAsync(m => m.PatientRecordID == id);
            if (patientRecord == null)
            {
                return NotFound();
            }

            return View(patientRecord);
        }

        // GET: PatientRecords/Create
        public IActionResult Create()
        {
            ViewData["CaseID"] = new SelectList(_context.Cases, "CaseID", "CaseID");
            ViewData["PatientID"] = new SelectList(_context.Patients, "ID", "ID");
            return View();
        }

        // POST: PatientRecords/Create
        // To protect from overposting attacks, please enable the specific properties you want to bind to, for 
        // more details see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create([Bind("PatientRecordID,CaseID,Notes,PatientID")] PatientRecord patientRecord)
        {
            if (ModelState.IsValid)
            {
                _context.Add(patientRecord);
                await _context.SaveChangesAsync();
                return RedirectToAction("Index");
            }
            ViewData["CaseID"] = new SelectList(_context.Cases, "CaseID", "CaseID", patientRecord.CaseID);
            ViewData["PatientID"] = new SelectList(_context.Patients, "ID", "ID", patientRecord.PatientID);
            return View(patientRecord);
        }

        // GET: PatientRecords/Edit/5
        public async Task<IActionResult> Edit(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var patientRecord = await _context.PatientRecords.SingleOrDefaultAsync(m => m.PatientRecordID == id);
            if (patientRecord == null)
            {
                return NotFound();
            }
            ViewData["CaseID"] = new SelectList(_context.Cases, "CaseID", "CaseID", patientRecord.CaseID);
            ViewData["PatientID"] = new SelectList(_context.Patients, "ID", "ID", patientRecord.PatientID);
            return View(patientRecord);
        }

        // POST: PatientRecords/Edit/5
        // To protect from overposting attacks, please enable the specific properties you want to bind to, for 
        // more details see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit(int id, [Bind("PatientRecordID,CaseID,Notes,PatientID")] PatientRecord patientRecord)
        {
            if (id != patientRecord.PatientRecordID)
            {
                return NotFound();
            }

            if (ModelState.IsValid)
            {
                try
                {
                    _context.Update(patientRecord);
                    await _context.SaveChangesAsync();
                }
                catch (DbUpdateConcurrencyException)
                {
                    if (!PatientRecordExists(patientRecord.PatientRecordID))
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
            ViewData["CaseID"] = new SelectList(_context.Cases, "CaseID", "CaseID", patientRecord.CaseID);
            ViewData["PatientID"] = new SelectList(_context.Patients, "ID", "ID", patientRecord.PatientID);
            return View(patientRecord);
        }

        // GET: PatientRecords/Delete/5
        public async Task<IActionResult> Delete(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var patientRecord = await _context.PatientRecords.SingleOrDefaultAsync(m => m.PatientRecordID == id);
            if (patientRecord == null)
            {
                return NotFound();
            }

            return View(patientRecord);
        }

        // POST: PatientRecords/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> DeleteConfirmed(int id)
        {
            var patientRecord = await _context.PatientRecords.SingleOrDefaultAsync(m => m.PatientRecordID == id);
            _context.PatientRecords.Remove(patientRecord);
            await _context.SaveChangesAsync();
            return RedirectToAction("Index");
        }

        private bool PatientRecordExists(int id)
        {
            return _context.PatientRecords.Any(e => e.PatientRecordID == id);
        }
    }
}
