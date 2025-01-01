# Environment: Defines the scheduling problem
import random
import numpy as np
import pygame


class Environment:
    def __init__(self, num_slot, num_students):
        self.num_slot = num_slot
        self.num_students = num_students
        self.slot_durations = np.random.randint(1, 3, size=num_slot)
        self.slot_priorities = np.random.randint(1, 5, size=num_slot)
        self.days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']
        self.students_days = [random.choices(self.days) for _ in range(num_students)]  # Randomly assign day preferences for each student

    def generate_assignments(self):
        """
        Randomly assign slot to students for initial population in the genetic algorithm.
        """
        return [np.random.randint(0, self.num_students, size=self.num_slot) for _ in range(50)]

    def draw_grid(self, screen, font, slot_assignments):
        """
        Draw a grid representing the slot assignments on the Pygame screen.
        Each row is a student, each column is a slot, colors are based on task durations, and annotations
        show task priorities and durations inside the grid.
        """
        screen.fill((255, 255, 255))  # Background color
        color_map = [(0, 0, 255 - i * 25) for i in range(10)]  # Color gradient for durations
        cell_size = 60
        margin_left = 150
        margin_top = 100

        # Display task names on the top (X-axis labels)
        for col in range(self.num_slot):
            Slot_text = font.render(f"Slot {col + 1}", True, (0, 0, 0))
            screen.blit(Slot_text, (margin_left + col * cell_size + cell_size // 3, margin_top - 30))

        # Draw each student row with tasks assigned
        for row in range(self.num_students):
            # Display student day preferences on the left of each row
            preference_text = font.render(f" {', '.join(self.students_days[row])}", True, (0, 0, 0))
            screen.blit(preference_text, (10, margin_top + row * cell_size + cell_size // 3))

            for col in range(self.num_slot):
                # Determine if this task is assigned to the current student
                assigned_student = slot_assignments[col]
                
                # Set color based on task duration
                color = color_map[self.slot_durations[col] - 1] if assigned_student == row else (200, 200, 200)
                
                # Draw the cell
                cell_rect = pygame.Rect(
                    margin_left + col * cell_size,
                    margin_top + row * cell_size,
                    cell_size,
                    cell_size
                )
                pygame.draw.rect(screen, color, cell_rect)
                pygame.draw.rect(screen, (0, 0, 0), cell_rect, 1)  # Draw cell border

                # Display task priority and duration within the cell
                priority_text = font.render(f"P{self.slot_priorities[col]}", True, (255, 255, 255) if assigned_student == row else (0, 0, 0))
                duration_text = font.render(f"{self.slot_durations[col]}h", True, (255, 255, 255) if assigned_student == row else (0, 0, 0))
                screen.blit(priority_text, (cell_rect.x + 5, cell_rect.y + 5))
                screen.blit(duration_text, (cell_rect.x + 5, cell_rect.y + 25))


# Genetic Algorithm parameters
population_size = 50
mutation_rate = 0.3
n_generations = 100

def fitness(individual, environment):
    conflict_penalty = 0
    preference_penalty = 0

    for task, student_id in enumerate(individual):
        assigned_day = environment.days[task % len(environment.days)]  # Slot days based on task index
        student_pref_days = environment.students_days[student_id]
        
        # Conflict Penalty: Check if the student's assigned slot conflicts with their preferred days
        if assigned_day not in student_pref_days:
            conflict_penalty += 1
        
        # Preference Penalty: Penalize if the assigned slot isn't one of the student's preferred days
        # We assume here that the student prefers to take a class in their preferred days
        if assigned_day not in student_pref_days:
            preference_penalty += 1  # For each non-preferred day slot assigned

    # Combine penalties
    return conflict_penalty + preference_penalty


def selection(population, environment):
    return sorted(population, key=lambda ind: fitness(ind, environment))[:population_size // 2]

def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)  # Random crossover point
    return np.concatenate([parent1[:point], parent2[point:]])  # Combine the genes of both parents


def mutate(individual, num_students):
    for i in range(len(individual)):
        if random.random() < mutation_rate:  # With probability of mutation_rate
            individual[i] = random.randint(0, num_students - 1)  # Randomly reassign to a student
    return individual

