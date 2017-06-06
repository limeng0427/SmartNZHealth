package service;

import java.util.List;

import domain.User;

public interface UserDAO {

    void add(User user);
    List<User> getUsers();
    User getUser(String email);
    void deleteAllUsers();

}
