using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Threading.Tasks;

namespace SmartNZHealth.Models
{
    public class Case
    {
        public int CaseID { get; set; }
        //public DateTime CaseDateTime { get; set; }

        [DataType(DataType.Date)]
        public DateTime ConsultationDate { get; set; }
        public String CaseDescription { get; set; }
        public String Prescription { get; set; }

        // FK
        public String PatientId { get; set; }
        public String DoctorId { get; set; }

        // Navi 
        public ApplicationUser Patient { get; set; }
        //public ICollection<PatientRecord> PatientRecords { get; set; }
    }
}
