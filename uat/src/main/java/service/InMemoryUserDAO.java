package service;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import domain.User;

public class InMemoryUserDAO implements UserDAO {
    Map<String, User> registeredUsers = new HashMap<>();

    @Override
    public List<User> getUsers() {
        return Arrays.asList(registeredUsers.values().toArray(new User[0]));
    }

    @Override
    public User getUser(String email){
        return registeredUsers.get(email);
    }

    @Override
    public void add(User user) {
        registeredUsers.put(user.getEmail(), user);
    }

    @Override
    public void deleteAllUsers() {
        registeredUsers.clear();
    }

}
