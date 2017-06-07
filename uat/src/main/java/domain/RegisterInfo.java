package domain;


public class RegisterInfo {

    private final String email;
    private final String password;
    private final String confirmPassword;
    private final String firstName;
    private final String lastName;
    private final String gender;
    private final String birthDate;
    private final String mobile;
    private final String emergencyContactNumber;
    private final String emergencyContactPerson;

    public RegisterInfo(String email, String password, String confirmPassword,
            String firstName, String lastName, String gender, String birthDate,
            String mobile, String emergencyContactNumber,
            String emergencyContactPerson) {
        super();
        this.email = email;
        this.password = password;
        this.confirmPassword = confirmPassword;
        this.firstName = firstName;
        this.lastName = lastName;
        this.gender = gender;
        this.birthDate = birthDate;
        this.mobile = mobile;
        this.emergencyContactNumber = emergencyContactNumber;
        this.emergencyContactPerson = emergencyContactPerson;
    }

    public String getEmail() {
        return email;
    }

    public String getPassword() {
        return password;
    }

    public String getConfirmPassword() {
        return confirmPassword;
    }

    public String getFirstName() {
        return firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public String getGender() {
        return gender;
    }

    public String getBirthDate() {
        return birthDate;
    }

    public String getMobile() {
        return mobile;
    }

    public String getEmergencyContactNumber() {
        return emergencyContactNumber;
    }

    public String getEmergencyContactPerson() {
        return emergencyContactPerson;
    }

}
