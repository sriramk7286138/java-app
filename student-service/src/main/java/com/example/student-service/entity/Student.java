package com.example.student_service.entity;

import jakarta.persistence.*;
import lombok.*;

@Entity
@Table(name = "students") // This explicitly names the table
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class Student {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String name;
    
    @Column(unique = true)
    private String email;
    
    private int age;
    private double cgpa;
    
    @Column(unique = true)
    private String rollNumber;
}