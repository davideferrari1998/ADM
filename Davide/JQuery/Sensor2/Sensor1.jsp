<%@ page import="java.util.*"%><% response.setContentType("application/json");
%>{	
	"sensor":"1",
	"type":"PM10",
	"timestamp":"<%=(new Date(session.getLastAccessedTime()))%>",
	"value":"5"
}
