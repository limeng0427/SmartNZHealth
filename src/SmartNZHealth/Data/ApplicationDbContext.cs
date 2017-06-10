using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Identity.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore;
using SmartNZHealth.Models;

namespace SmartNZHealth.Data
{
    public class ApplicationDbContext : IdentityDbContext<ApplicationUser>
    {
        public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options)
            : base(options)
        {
        }

        public ApplicationDbContext()
        {
        }

        protected override void OnModelCreating(ModelBuilder builder)
        {
            base.OnModelCreating(builder);
            // Customize the ASP.NET Identity model and override the defaults if needed.
            // For example, you can rename the ASP.NET Identity table names and more.
            // Add your customizations after calling base.OnModelCreating(builder);
        }

        //public DbSet<Administrator> Administrators { get; set; }
        //public DbSet<Doctor> Doctors { get; set; }
        public DbSet<ApplicationUser> Patients { get; set; }
        public DbSet<Case> Cases { get; set; }
        //public DbSet<ApplicationUser> ApplicationUser { get; set; }
        //public DbSet<PatientRecord> PatientRecords { get; set; }

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            //optionsBuilder.UseSqlite("Data Source = data.db");
            optionsBuilder.UseSqlite("Data Source = ..\\..\\..\\data.db");
        }
    }
}
