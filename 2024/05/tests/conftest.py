from _pytest.main import Session
from _pytest.reports import TestReport

total_time = 0.0


def pytest_runtest_logreport(report: TestReport) -> None:
    if report.when == "call":
        outcome = "PASSED" if report.passed else "FAILED"
        global total_time
        total_time += report.duration
        duration = round(report.duration, 5)
        test_name = report.nodeid.split("::")[-1]
        print(f"{test_name}: {outcome} ({duration} seconds)")
        if not report.passed:
            print(report.longreprtext)


def pytest_sessionfinish(session: Session, exitstatus: int) -> None:
    print(f"\n\n\033[93mTotal Time:\033[0m {round(total_time, 5)} seconds")
