package com.java.controller;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class FController {

	@Value("${data.admin_id}")
	private String id;
	
	@RequestMapping("/index")
	public String index() {
		
		System.out.println("application id: "+id);
		
		return "index";
	}
}
