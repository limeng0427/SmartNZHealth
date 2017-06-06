<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<!DOCTYPE html>
<html>
<head>
<title>Register</title>
<style type="text/css">@import url("<c:url value="/css/main.css"/>");</style>
</head>
<body>

<div id="global">

<table id="all_users_table">
    <tr>
        <td>Email</td>
        <td>Password</td>
    </tr>
    <c:forEach items="${requestScope.users}" var="user">
    <tr>
        <td>${user.email}</td>
        <td>${user.password}</td>
    </tr>
    </c:forEach>
</table>


</div>
</body>
</html>