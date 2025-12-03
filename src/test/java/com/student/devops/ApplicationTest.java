package com.student.devops;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class ApplicationTest {

    @Autowired
    private WebController controller;

    @Test
    void testController() {
        String result = controller.home();
        assertEquals("Hello! The CI/CD Pipeline is working correctly.", result);
    }
}