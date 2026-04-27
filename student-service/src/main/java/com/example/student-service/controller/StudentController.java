package com.example.student_service.controller;

import com.example.student_service.dto.StudentDTO;
import com.example.student_service.service.StudentService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/students")
@RequiredArgsConstructor
public class StudentController {

    private final StudentService service;

    @PostMapping
    public String saveStudents(@RequestBody List<StudentDTO> students) {
        service.saveAll(students);
        return "Saved " + students.size() + " students";
    }

    // UPDATED: Now returns the list of students
    @GetMapping
    public List<StudentDTO> getAllStudents() {
        return service.getAllStudents();
    }

    @GetMapping("/health")
    public String health() {
        return "Service B is running";
    }
}