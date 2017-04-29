using Microsoft.EntityFrameworkCore;
using SmartNZHealth.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace SmartNZHealth.Data
{
    public class HealthContext:DbContext
    {
        public HealthContext(DbContextOptions<HealthContext> options) : base(options)
        {
        }
        public DbSet<Patient> Patients { get; set; }
        public DbSet<PatientRecord> PatientRecords { get; set; }
        public DbSet<Case> Cases { get; set; }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.Entity<Patient>().ToTable("Patient");
            modelBuilder.Entity<PatientRecord>().ToTable("PatientRecord");
            modelBuilder.Entity<Case>().ToTable("Case");
        }

    }
}
