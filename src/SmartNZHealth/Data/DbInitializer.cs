using SmartNZHealth.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace SmartNZHealth.Data
{
    public class DbInitializer
    {
        public static void Initialize(HealthContext context)
        {
            context.Database.EnsureCreated();

            if (context.Patients.Any())
            {
                return; // DB has been seeded
            }

            var patients = new Patient[]
            {
                new Patient {LastName="John", FirstName = "Lee",
                Mobile="020-123456",
                Email = "John@abc.com",
                Allergy="Asthma"
                },
                new Patient {LastName="Joe", FirstName = "Lim",
                Mobile="020-123456",
                Email = "Joe@abc.com",
                Allergy="Cats"
                },
                new Patient {LastName="Lucy", FirstName = "Chou",
                Mobile="020-123456",
                Email = "Lucy@abc.com",
                Allergy="Pollen"
                },
            };
            foreach (Patient p in patients)
            {
                context.Patients.Add(p);
            }
            context.SaveChanges();

            var cases = new Case[]
            {
                new Case {CaseDescription = "Cold",
                Prescription="Cold medicine"
                },
                new Case {CaseDescription = "Fever",
                Prescription="Fever medicine"
                },
                new Case {CaseDescription = "Flu",
                Prescription="Flu medicine"
                },
            };
            foreach (Case c in cases)
            {
                context.Cases.Add(c);
            }
            context.SaveChanges();

            var patientRecords = new PatientRecord[]
            {
                new PatientRecord {PatientID=1, CaseID=1,},
                new PatientRecord {PatientID=2, CaseID=2,},
                new PatientRecord {PatientID=3, CaseID=3,},
            };
            foreach(PatientRecord p in patientRecords)
            {
                context.PatientRecords.Add(p);
            }
            context.SaveChanges();
        }
    }
}
