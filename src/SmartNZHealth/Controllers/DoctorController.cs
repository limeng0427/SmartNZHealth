using System.Linq;
using System.Collections.Generic;
using System.Security.Claims;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Identity.EntityFrameworkCore;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Logging;
using SmartNZHealth.Data;
using SmartNZHealth.Models;
using SmartNZHealth.Models.DoctorViewModels;
using SmartNZHealth.Services;

namespace SmartNZHealth.Controllers
{
    public class DoctorController : Controller
    {
        private readonly ApplicationDbContext _context;
        private readonly UserManager<ApplicationUser> _userManager;
        private readonly SignInManager<ApplicationUser> _signInManager;
        private readonly IEmailSender _emailSender;
        private readonly ISmsSender _smsSender;
        private readonly ILogger _logger;

        public DoctorController(
            ApplicationDbContext context,
            UserManager<ApplicationUser> userManager,
            SignInManager<ApplicationUser> signInManager,
            IEmailSender emailSender,
            ISmsSender smsSender,
            ILoggerFactory loggerFactory)
        {
            _context = context;
            _userManager = userManager;
            _signInManager = signInManager;
            _emailSender = emailSender;
            _smsSender = smsSender;
            _logger = loggerFactory.CreateLogger<DoctorController>();
        }

        [Authorize(Roles = "Admin")]
        public IActionResult Index()
        {
            ICollection<ApplicationUser> doctors = new List<ApplicationUser>();
            var users = _context.Users.AsNoTracking().ToList();
            foreach (var user in users)
            {
                var result = _userManager.IsInRoleAsync(user, "Doctor");
                if (result.Result == true)
                {
                    doctors.Add(user);
                }
            }

            if (doctors == null)
            {
                NotFound();
            }
            //_context.Users.Where(u => u.)
            return View(doctors);
        }

        //
        // GET: /Patient/Register
        [HttpGet]
        [AllowAnonymous]
        public IActionResult Register(string returnUrl = null)
        {
            ViewData["ReturnUrl"] = returnUrl;
            return View();
        }

        //
        // POST: /Patient/Register
        [HttpPost]
        [AllowAnonymous]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Register(RegisterViewModel model, string returnUrl = null)
        {
            ViewData["ReturnUrl"] = returnUrl;
            if (ModelState.IsValid)
            {
                var user = new ApplicationUser
                {
                    UserName = model.Email,
                    Email = model.Email,
                    FirstName = model.FirstName,
                    LastName = model.LastName,
                    Sex = model.Gender,
                    Mobile = model.Mobile,
                    Address = model.Address
                };
                var result = await _userManager.CreateAsync(user, model.Password);

                if (result.Succeeded)
                {
                    await _userManager.AddToRoleAsync(user, "Doctor");
                    return View("ConfirmRegister");
                }

                // send email confirmation code
                //if (result.Succeeded)
                //{
                //    // For more information on how to enable account confirmation and password reset please visit http://go.microsoft.com/fwlink/?LinkID=532713
                //    // Send an email with this link
                //    //var code = await _userManager.GenerateEmailConfirmationTokenAsync(user);
                //    //var callbackUrl = Url.Action("ConfirmEmail", "Account", new { userId = user.Id, code = code }, protocol: HttpContext.Request.Scheme);
                //    //await _emailSender.SendEmailAsync(model.Email, "Confirm your account",
                //    //    $"Please confirm your account by clicking this link: <a href='{callbackUrl}'>link</a>");

                //    //await _signInManager.SignInAsync(user, isPersistent: false);
                //    //_logger.LogInformation(3, "User created a new account with password.");
                //    //return RedirectToLocal(returnUrl);

                //    var code = await _userManager.GenerateEmailConfirmationTokenAsync(user);
                //    var callbackUrl = Url.Action("ConfirmEmail", "Account", new { userId = user.Id, code = code }, protocol: HttpContext.Request.Scheme);
                //    await _emailSender.SendEmailAsync(model.Email, "Confirm your account",
                //        $"Please confirm your account by copying and pasting this link in your browser:{callbackUrl}");
                //    _logger.LogInformation(3, "User created a new account with password.");
                //    return View("ConfirmRegister");
                //}

                AddErrors(result);
            }

            // If we got this far, something failed, redisplay form
            return View(model);
        }

        public async Task<IActionResult> EnableDisable(string id)
        {
            if (id == null)
            {
                return NotFound();
            }
            IEnumerable<ApplicationUser> members = ReturnAllMembers().Result;
            ApplicationUser member = (ApplicationUser)members.Single(u => u.Id == id);
            if (member == null)
            {
                return NotFound();
            }

            member.Enabled = !member.Enabled;
            _context.Update(member);
            await _context.SaveChangesAsync();

            return RedirectToAction("Index");
        }
        private async Task<IEnumerable<ApplicationUser>> ReturnAllMembers()
        {
            IdentityRole role = await _context.Roles.AsNoTracking().SingleOrDefaultAsync(r => r.Name == "Doctor");
            IEnumerable<ApplicationUser> users = _context.Users
                                                    .Where(x => x.Roles.Select(y => y.RoleId).Contains(role.Id))
                                                    .ToList();
            return users;
        }

        #region Helpers

        private void AddErrors(IdentityResult result)
        {
            foreach (var error in result.Errors)
            {
                ModelState.AddModelError(string.Empty, error.Description);
            }
        }

        private Task<ApplicationUser> GetCurrentUserAsync()
        {
            return _userManager.GetUserAsync(HttpContext.User);
        }

        private IActionResult RedirectToLocal(string returnUrl)
        {
            if (Url.IsLocalUrl(returnUrl))
            {
                return Redirect(returnUrl);
            }
            else
            {
                return RedirectToAction(nameof(HomeController.Index), "Home");
            }
        }

        #endregion
    }
}