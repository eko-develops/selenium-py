from test import Test
from constants import *

from timer_group import TimerGroup


def main():
    """Main function to run tests"""
    total_timer = "total_test_time"
    timer = TimerGroup(total_timer)
    timer.start_timer(total_timer)

    """Test page load"""
    # Test.page_load(HOME_URL)
    """Test login flow"""
    Test.login_page(USER, PASS, HOME_URL)

    timer.end_timer(total_timer)
    timer.display_full()


main()
