package com.example.student_service.service;

import com.example.student_service.dto.StudentDTO;
import com.example.student_service.entity.Student;
import com.example.student_service.repository.StudentRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

@Service
@RequiredArgsConstructor
public class StudentService {

    private final StudentRepository repository;

    public void saveAll(List<StudentDTO> dtos) {
        List<Student> students = dtos.stream()
                .map(dto -> Student.builder()
                        .name(dto.getName())
                        .email(dto.getEmail())
                        .age(dto.getAge())
                        .cgpa(dto.getCgpa())
                        .rollNumber(dto.getRollNumber())
                        .build())
                .collect(Collectors.toList());

        repository.saveAll(students);
        repository.flush(); 
    }

    // ADDED: Method to retrieve data
    public List<StudentDTO> getAllStudents() {
        return repository.findAll().stream()
                .map(student -> StudentDTO.builder()
                        .name(student.getName())
                        .email(student.getEmail())
                        .age(student.getAge())
                        .cgpa(student.getCgpa())
                        .rollNumber(student.getRollNumber())
                        .build())
                .collect(Collectors.toList());
    }
}