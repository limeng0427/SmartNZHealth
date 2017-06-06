package controller;

import javax.servlet.http.HttpServletRequest;
import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;

import domain.LoginInfo;
import domain.RegisterInfo;
import service.DBUserDAO;
import service.UserService;

@Controller
public class UserController {
    private UserService userService = new UserService(new DBUserDAO());

    private static final Log logger =
        LogFactory.getLog(UserController.class);

    @RequestMapping(value = "/register")
    public String inputProduct(Model model) {
        model.addAttribute("registerInfo", new RegisterInfo());
        return "RegisterForm";
    }

    @RequestMapping(value = "/register-success")
    public String registerSuccess(Model model) {
        return "RegisterDetails";
    }

    @RequestMapping(value = "/login")
    public String login(Model model) {
        model.addAttribute("loginInfo", new LoginInfo());
        return "LoginForm";
    }

    @RequestMapping(value = "/list-users")
    public String listUsers(HttpServletRequest servletRequest) {
        servletRequest.setAttribute("users", userService.getUsers());
        return "ListUsers";
    }

    @RequestMapping(value = "/try-login")
    public String tryLogin(HttpServletRequest servletRequest,
            @ModelAttribute LoginInfo loginInfo,
            BindingResult bindingResult, Model model) {
        logger.info("tryLogin called.");
        try {
            userService.loginUser(loginInfo);
            logger.info("login success");
            return "redirect:/list-users";
        } catch (Exception e) {
            logger.info("login error", e);
            model.addAttribute("error", "login fail");
            return "LoginForm";
        }
    }

    @RequestMapping(value = "/save-register")
    public String saveProduct(HttpServletRequest servletRequest,
            @ModelAttribute RegisterInfo registerInfo,
            BindingResult bindingResult, Model model) {

        try {
            userService.register(registerInfo);
            return "redirect:/register-success";
        } catch (Exception e) {
            logger.info("register error", e);
            model.addAttribute("error", "login fail");
            return "RegisterForm";
        }
    }
}