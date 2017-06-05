using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace SmartNZHealth.Models.CaseViewModels
{
    public class CreateViewModel
    {
        public ApplicationUser User;
        public Case _case = new Case();
    }
}
