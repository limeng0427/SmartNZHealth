package steps;

import java.util.List;

import cucumber.api.DataTable;
import cucumber.api.java.en.Given;
import domain.PatientRegisterInfo;

public class PredefinedUserSteps {
    @Given("^There are following patients in the system:$")
    public void thereAreFollowingPatientsInTheSystem(DataTable registerInfoTable) throws Throwable {
//        PatientRegisterInfo registerInfo = getRegisterInfoFromStringList(registerInfoTable.raw().get(1));
//
//        UserService userService = new UserService(new DBUserDAO());
//        userService.registerPatient(registerInfo);
    }

    private PatientRegisterInfo getRegisterInfoFromStringList(List<String> list) {
        return new PatientRegisterInfo(list.get(0), // email
                                list.get(1), // password
                                list.get(1), // confirm password
                                list.get(2), // frist name
                                list.get(3), // last name
                                list.get(4), // gender
                                list.get(5), // birth date
                                list.get(6), // mobile
                                list.get(7), // address
                                list.get(8), // emergency contact number
                                list.get(9)); // emergency contact person
    }

}
