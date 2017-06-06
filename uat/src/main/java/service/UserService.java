package service;

import java.util.List;

import domain.LoginInfo;
import domain.RegisterInfo;
import domain.User;

public final class UserService {
    private final UserDAO userDao;

    public UserService(UserDAO userDao) {
        this.userDao = userDao;
    }

    public void register(RegisterInfo registerInfo) throws RegisterException {
        String email = registerInfo.getEmail();

        User user = userDao.getUser(email);

        if (user != null) {
            throw new RegisterException("User " + registerInfo.getEmail() + " already exists");
        }

        if (! registerInfo.getPassword().equals(registerInfo.getConfirmPassword())) {
            throw new RegisterException("password " + registerInfo.getPassword() +
                    " does not match confrimPassword " + registerInfo.getConfirmPassword()
                    );
        }

        userDao.add(new User(email, registerInfo.getPassword()));
    }

    public List<User> getUsers() {
        return userDao.getUsers();
    }

    public void loginUser(LoginInfo loginInfo) throws LoginException {
        String email = loginInfo.getEmail();
        String password = loginInfo.getPassword();

        User user = userDao.getUser(email);

        if (user == null) {
            throw new LoginException("User " + email + " does not exists");
        }


        if (!user.getPassword().equals(password)) {
            throw new LoginException("Password for User " + email + " is incorrect");
        }
    }

    public void deleteAllUsers() {
        userDao.deleteAllUsers();
    }

}
