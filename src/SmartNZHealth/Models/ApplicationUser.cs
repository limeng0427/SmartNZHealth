using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Identity.EntityFrameworkCore;

namespace SmartNZHealth.Models
{
    public enum Gender
    {
        Male,
        Female
    }
    public class ApplicationUser : IdentityUser
    {
        //public int ID { get; set; }
        public string LastName { get; set; }
        public string FirstName { get; set; }
        public Gender Sex { get; set; }

        [DataType(DataType.Date)]
        public DateTime Birthday { get; set; }
        //public int Age { get; set; }
        public string Mobile { get; set; }
        //public string Email { get; set; }
        public string Address { get; set; }
        public string EmergencyContactName { get; set; }
        public string EmergencyContactPhone { get; set; }
        //public string Hometown { get; set; }
        //public string Allergy { get; set; }
        //public int BloodID { get; set; }
        public bool Enabled { get; set; }

        public ICollection<Case> Cases { get; set; }

    }
}
