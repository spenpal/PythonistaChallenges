from _pytest.reports import TestReport


def pytest_runtest_logreport(report: TestReport) -> None:
    if report.when == "call":
        outcome = "PASSED" if report.passed else "FAILED"
        duration = f"{report.duration:.5f}"
        test_name = report.nodeid.split("::")[-1]
        print(f"{test_name}: {outcome} ({duration} seconds)")
        if not report.passed:
            print(report.longreprtext)
