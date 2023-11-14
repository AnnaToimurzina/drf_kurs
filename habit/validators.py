from datetime import timezone

from rest_framework.exceptions import ValidationError

class LinkedHabitsValidator:
    def __init__(self, linked_habits_field, reward_field):
        self.linked_habits_field = linked_habits_field
        self.reward_field = reward_field

    def __call__(self, value):
        '''Валидатор проверяет, что не выбраны и связанные привычки, и указано вознаграждение одновременно.'''
        linked_habits = self.linked_habits_field.value_from_object(value)
        reward = self.reward_field.value_from_object(value)

        if linked_habits and reward:
            raise ValidationError("Выберите либо связанную привычку, либо укажите вознаграждение, не оба одновременно.")




class TimeValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        '''Валидатор проверяет, что время выполнения не превышает 120 секунд.'''
        if value > 120:
            raise ValidationError('Время выполнения не должно превышать 120 секунд.')


class LinkedHabitsValidator2:
    def __init__(self, linked_habits_field, is_pleasurable_field):
        self.linked_habits_field = linked_habits_field
        self.is_pleasurable_field = is_pleasurable_field

    def __call__(self, value):
        '''Валидатор проверяет, что связанные привычки - только приятные привычки.'''
        linked_habits = self.linked_habits_field.value_from_object(value)
        is_pleasurable = self.is_pleasurable_field.value_from_object(value)

        if linked_habits and not all(habit.is_pleasurable for habit in linked_habits):
            raise ValidationError("Связанные привычки могут включать только приятные привычки.")

class PleasurableRewardValidator:
    def __init__(self, field):
        self.field = field
    def __call__(self, is_pleasurable, reward):
        '''Валидатор проверяет, что у приятной привычки нет вознаграждения.'''
        if is_pleasurable and reward:
            raise ValidationError('У приятной привычки не может быть вознаграждения.')

class PleasurableRewardValidator:
    def __init__(self, is_pleasurable_field, reward_field):
        self.is_pleasurable_field = is_pleasurable_field
        self.reward_field = reward_field

    def __call__(self, instance):
        '''Валидатор проверяет, что у приятной привычки нет вознаграждения.'''
        is_pleasurable = self.is_pleasurable_field.value_from_object(instance)
        reward = self.reward_field.value_from_object(instance)

        if is_pleasurable and reward:
            raise ValidationError('У приятной привычки не может быть вознаграждения.')


class PeriodicityValidator:
    def __init__(self, field):
        self.field = field
    def __call__(self, value):
        '''Валидатор проверяет, что привычка не выполняется реже одного раза в 7 дней.'''
        last_executed = value.last_executed  # Предполагаем, что у вашей модели есть поле last_executed
        if last_executed:
            days_since_last_execution = (timezone.now() - last_executed).days
            if days_since_last_execution < 7:
                raise ValidationError('Привычку нельзя выполнять реже одного раза в 7 дней.')

