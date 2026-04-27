package com.example.student_service.dto;

import lombok.Data;
import lombok.Builder;
import lombok.NoArgsConstructor;
import lombok.AllArgsConstructor;

@Data
@Builder 
@NoArgsConstructor 
@AllArgsConstructor
public class StudentDTO {
    private String name;
    private String email;
    private Integer age;
    private Double cgpa;
    private String rollNumber;
}