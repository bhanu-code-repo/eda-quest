
import os
import unittest

def run_tests_and_generate_report():
    loader = unittest.TestLoader()
    start_dir = 'tests'  # Directory containing your test files
    pattern = 'test_*.py'
    
    # Discover tests and create a test suite
    suite = loader.discover(start_dir, pattern=pattern)
    
    # Create a test runner and run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Generate a test report in a text file
    report_dir = 'test_reports'  # Directory to store test reports
    os.makedirs(report_dir, exist_ok=True)
    report_path = os.path.join(report_dir, 'test_report.txt')

    with open(report_path, 'w') as report_file:
        runner = unittest.TextTestRunner(stream=report_file, verbosity=2)
        runner.run(suite)
    
    # Print a test report summary
    print("\n======= Test Summary =======")
    print(f"Total Tests Run: {result.testsRun}")
    print(f"Total Failures: {len(result.failures)}")
    print(f"Total Errors: {len(result.errors)}")
    print(f"Total Skipped: {len(result.skipped)}")
    print(f"Total Passed: {result.testsRun - len(result.failures) - len(result.errors)}")

if __name__ == '__main__':
    run_tests_and_generate_report()