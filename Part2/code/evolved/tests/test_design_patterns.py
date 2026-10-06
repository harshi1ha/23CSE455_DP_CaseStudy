import ast
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class RefactoringStructureTests(unittest.TestCase):
    def read(self, relative):
        return (ROOT / relative).read_text()

    def test_routes_delegate_persistence_to_repositories(self):
        source = self.read("routes.py")
        self.assertNotIn("db.session", source)
        self.assertNotIn("User.query", source)
        self.assertNotIn("Event.query", source)
        self.assertNotIn("Ticket.query", source)
        self.assertIn("event_repo.create", source)
        self.assertIn("event_repo.update", source)
        self.assertIn("event_repo.delete", source)
        self.assertIn("self.ticket_repository.create_many", self.read("services/registration_service.py"))

    def test_repository_layer_exists_and_has_core_operations(self):
        event_repo = self.read("repositories/event_repository.py")
        ticket_repo = self.read("repositories/ticket_repository.py")
        user_repo = self.read("repositories/user_repository.py")
        for method in ("get_by_id", "create", "update", "delete", "search_upcoming"):
            self.assertIn(f"def {method}", event_repo)
        for method in ("get_by_id", "find_paid_for_event_and_user", "create_many", "save"):
            self.assertIn(f"def {method}", ticket_repo)
        for method in ("get_by_email", "get_by_username", "save"):
            self.assertIn(f"def {method}", user_repo)

    def test_strategy_pattern_structure(self):
        base = self.read("strategies/base_filter.py")
        route = self.read("routes.py")
        repository = self.read("repositories/event_repository.py")
        self.assertIn("class EventFilterStrategy", base)
        self.assertIn("def apply", base)
        strategy_files = {
            "TextSearchStrategy": "strategies/text_search_strategy.py",
            "CategoryFilterStrategy": "strategies/category_filter_strategy.py",
            "DateFromFilterStrategy": "strategies/date_range_strategy.py",
            "DateToFilterStrategy": "strategies/date_range_strategy.py",
        }
        for strategy, relative in strategy_files.items():
            self.assertIn(f"class {strategy}", self.read(relative))
        self.assertIn("strategy.apply(query)", repository)
        self.assertIn("TextSearchStrategy", route)
        self.assertIn("CategoryFilterStrategy", route)

    def test_observer_pattern_structure(self):
        subject = self.read("services/registration_service.py")
        observer = self.read("observers/registration_observer.py")
        notification = self.read("observers/notification_observer.py")
        statistics = self.read("observers/statistics_observer.py")
        self.assertIn("class RegistrationObserver", observer)
        self.assertIn("self._observers", subject)
        self.assertIn("def attach", subject)
        self.assertIn("def notify", subject)
        self.assertIn("observer.update", subject)
        self.assertIn("class RegistrationNotificationObserver", notification)
        self.assertIn("class RegistrationStatisticsObserver", statistics)


def _snake(name):
    out = []
    for char in name:
        if char.isupper() and out:
            out.append("_")
        out.append(char.lower())
    return "".join(out)


if __name__ == "__main__":
    unittest.main()
