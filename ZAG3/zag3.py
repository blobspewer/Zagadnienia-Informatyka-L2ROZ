import json
import os

class ScheduleManager:
    def __init__(self):
        self.schedule = {
            "1": [],
            "2": [],
            "3": [],
            "4": [],
            "5": [],
            "6": [],
            "7": []
        }
        self.file_name = os.path.join(os.path.dirname(__file__), "schedule.json")
        self.load_schedule()

    def save_schedule(self):
        """Zapisuje harmonogram do pliku JSON"""
        try:
            serializable_schedule = {
                day: list(map(list, lessons)) for day, lessons in self.schedule.items()
            }
            with open(self.file_name, "w") as file:
                json.dump(serializable_schedule, file, indent=4)
            print("Harmonogram zapisany do pliku:", self.file_name)
        except Exception as e:
            print(f"Błąd podczas zapisywania harmonogramu: {e}")

    def load_schedule(self):
        """Wczytuje harmonogram z pliku JSON"""
        try:
            with open(self.file_name, "r") as file:
                serializable_schedule = json.load(file)
            self.schedule = {
                day: [tuple(lesson) for lesson in lessons]
                for day, lessons in serializable_schedule.items()
            }
            print("Harmonogram wczytany z pliku:", self.file_name)
        except FileNotFoundError:
            print("Nie znaleziono pliku harmonogramu. Plik będzie stworzony po dodaniu lekcji.")
        except json.JSONDecodeError as e:
            print(f"Błąd dekodowania pliku JSON: {e}. Tworzenie pustego harmonogramu.")
        except Exception as e:
            print(f"Błąd podczas wczytywania harmonogramu: {e}")

    def add_lesson(self, day, time, subject):
        """Dodaje przedmiot do wybranego dnia tygodnia"""
        if day in self.schedule:
            self.schedule[day].append((time, subject))
            self.save_schedule()
            print(f"Dodano lekcje: {subject} o godzinie {time} w {day}.")
        else:
            print("Nieprawidłowy dzień tygodnia.")

    def update_lesson(self, day, old_time, new_time, new_subject):
        """Aktualizuje przedmiot w harmonogramie"""
        if day in self.schedule:
            for i, (time, subject) in enumerate(self.schedule[day]):
                if time == old_time:
                    self.schedule[day][i] = (new_time, new_subject)
                    self.save_schedule()
                    print(f"Zaktualizowano lekcje z {old_time} na {new_time}, przedmiot: {new_subject}.")
                    return
            print(f"Nie znaleziono lekcji o godzinie {old_time} w {day}.")
        else:
            print("Nieprawidłowy dzień tygodnia.")

    def reset_schedule(self):
        """Resetuje cały harmonogram do pustego"""
        self.schedule = {
            "1": [],
            "2": [],
            "3": [],
            "4": [],
            "5": [],
            "6": [],
            "7": []
        }
        self.save_schedule()
        print("Harmonogram został zresetowany.")

    def view_schedule(self):
        """Wyświetla cały harmonogram lekcji"""
        print("\nHarmonogram lekcji:")
        for day, lessons in self.schedule.items():
            print(f"{day}:")
            if lessons:
                for time, subject in sorted(lessons):
                    print(f"  {time}: {subject}")
            else:
                print("  Brak lekcji.")

    def run(self):
        """Główna pętla programu"""
        while True:
            print("\n--- Zarządzanie harmonogramem lekcji ---")
            print("1. Dodaj lekcje")
            print("2. Aktualizuj lekcje")
            print("3. Wyświetl harmonogram")
            print("4. Zresetuj harmonogram")
            print("5. Wyjście")

            choice = input("Wybierz opcję: ")

            if choice == "1":
                day = input("Podaj dzień tygodnia: ").capitalize()
                time = input("Podaj godzinę (np. 08:00): ")
                subject = input("Podaj nazwę przedmiotu: ")
                self.add_lesson(day, time, subject)

            elif choice == "2":
                day = input("Podaj dzień tygodnia: ").capitalize()
                old_time = input("Podaj godzinę lekcji do aktualizacji (np. 09:00): ")
                new_time = input("Podaj nową godzinę (np. 10:00): ")
                new_subject = input("Podaj nową nazwę przedmiotu: ")
                self.update_lesson(day, old_time, new_time, new_subject)

            elif choice == "3":
                self.view_schedule()

            elif choice == "4":
                confirm = input("Czy na pewno chcesz zresetować harmonogram? (y/n): ")
                if confirm.lower() == "y":
                    self.reset_schedule()
                else:
                    print("Resetowanie harmonogramu anulowane.")

            elif choice == "5":
                print("Zakończono działanie programu.")
                break

            else:
                print("Nieistniejący wybór. Spróbuj ponownie.")

if __name__ == "__main__":
    manager = ScheduleManager()
    manager.run()
