<%@ page import="java.util.*"%><% response.setContentType("application/json");
%>{	
	"sensor":"4",
	"type":"PM10",
	"timestamp":"<%=(new Date(session.getLastAccessedTime()))%>",
	"value":"2"
}