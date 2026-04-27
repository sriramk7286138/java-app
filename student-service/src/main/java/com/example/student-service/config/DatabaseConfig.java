package com.example.student_service.config;

import jakarta.annotation.PostConstruct;
import org.springframework.context.annotation.Configuration;

@Configuration
public class DatabaseConfig {

    @PostConstruct
    public void loadDriver() {
        try {
            Class.forName("org.sqlite.JDBC");
            System.out.println("SQLite Driver Loaded Successfully");
        } catch (ClassNotFoundException e) {
            throw new RuntimeException("Failed to load SQLite driver", e);
        }
    }
}