"""Utility broker to improve Ssentry exception handling."""

from insights.core.dr import Broker
from insights.core.dr import MissingRequirements
from insights.core.spec_factory import ContentException

from sentry_sdk import capture_exception


class SentryMonitoredBroker(Broker):
    """Implementation of Broker with custom Sentry capturing logic."""

    def add_exception(self, component, ex, tb=None):
        """Check added exception in order to use it with Sentry or not."""
        super().add_exception(component, ex, tb)

        # prevent MissingRequirements and ContentException from being sent to sentry
        if not isinstance(ex, (MissingRequirements, ContentException)):
            capture_exception(ex)
