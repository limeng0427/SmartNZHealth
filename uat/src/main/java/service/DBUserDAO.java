package service;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;

import domain.User;

public class DBUserDAO implements UserDAO {
    private static final Log logger =
            LogFactory.getLog(DBUserDAO.class);

    private static final String INSERT_PRODUCT_SQL = "INSERT INTO userprofile_userprofile "
            + "(email, password) " + "VALUES (?, ?)";
    private static final String GET_USERS_SQL = "SELECT email, password FROM userprofile_userprofile";
    private static final String GET_USER_SQL = "SELECT * FROM userprofile_userprofile WHERE email = ?";
    private static final String DELETE_ALL_USERS_SQL ="DELETE FROM userprofile_userprofile";

    private static final String dbUrl = "jdbc:sqlite:../src-django/myproj/db.sqlite3";



    private Connection getConnection() {
        try {
            System.out.println("home: " + System.getProperty("user.dir"));
            Class.forName("org.sqlite.JDBC");
        } catch (ClassNotFoundException e) {
            throw new RuntimeException(e);
        }

        try {
            return DriverManager.getConnection(dbUrl);
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public void add(User user) {
        logger.info("Adding uesr: " + user);
        try (Connection connection = getConnection();
                PreparedStatement pStatement = connection
                        .prepareStatement(INSERT_PRODUCT_SQL)) {
            pStatement.setString(1, user.getEmail());
            pStatement.setString(2, user.getPassword());
            pStatement.executeUpdate();
        } catch (SQLException e) {
            logger.info("Adding uesr wrong", e);
            throw new RuntimeException(
                    "Error adding product. " + e.getMessage());
        }

    }

    @Override
    public List<User> getUsers() {
        List<User> users = new ArrayList<>();
        try (Connection connection = getConnection();
                PreparedStatement pStatement = connection
                        .prepareStatement(GET_USERS_SQL);
                ResultSet resultSet = pStatement.executeQuery()) {
            while (resultSet.next()) {
                User user = new User(resultSet.getString("email"), resultSet.getString("password"));
                users.add(user);
            }
        } catch (SQLException e) {
            throw new RuntimeException(
                    "Error getting products. " + e.getMessage());
        }
        return users;
    }

    @Override
    public User getUser(String email) {
        try (Connection connection = getConnection();
                PreparedStatement pStatement = connection
                        .prepareStatement(GET_USER_SQL)) {
            pStatement.setString(1, email);
            try (ResultSet resultSet = pStatement.executeQuery()) {
                while (resultSet.next()) {
                    User user = new User(resultSet.getString("email"), resultSet.getString("password"));
                    return user;
                }

                return null;
            }
        } catch (SQLException e) {
            throw new RuntimeException(
                    "Error getting products. " + e.getMessage());
        }
    }

    @Override
    public void deleteAllUsers() {
        try (Connection connection = getConnection();
                PreparedStatement pStatement = connection
                        .prepareStatement(DELETE_ALL_USERS_SQL)) {
            pStatement.executeUpdate();
        } catch (SQLException e) {
            throw new RuntimeException(
                    "Error getting products. " + e.getMessage());
        }

    }

}
