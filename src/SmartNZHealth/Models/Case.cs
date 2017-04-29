using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace SmartNZHealth.Models
{
    public class Case
    {
        public int CaseID { get; set; }
        //public DateTime CaseDateTime { get; set; }
        public String CaseDescription { get; set; }
        public String Prescription { get; set; }

        public ICollection<PatientRecord> PatientRecords { get; set; }
    }
}
