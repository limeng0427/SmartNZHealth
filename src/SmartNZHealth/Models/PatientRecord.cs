using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace SmartNZHealth.Models
{
    public class PatientRecord
    {
        public int PatientRecordID { get; set; }
        public int PatientID { get; set; }
        public int CaseID { get; set; }
        public string Notes { get; set; }

        public Patient Patient { get; set; }
        public Case Case { get; set; }
    }
}
