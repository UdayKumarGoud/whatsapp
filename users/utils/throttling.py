from rest_framework.throttling import SimpleRateThrottle, AnonRateThrottle
from django.core.cache import cache
from django.utils.cache import get_cache_key


class CustomAttemptThrottle(SimpleRateThrottle):
    """
    Custom throttle based on number of attempts.
    """
    scope = 'loginAttempts'
    def get_cache_key(self, request, view):
        """
        Returns the cache key based on the user ID and class name.
        """
        user_id = request.user.id if request.user.is_authenticated else None
        class_name = view.__class__.__name__
        return f"{user_id}-{class_name}"
    
    def parse_rate(self, rate):
        if rate is None:
            return None, None
        num, period = rate.split('/')
        num_requests = int(num)
        duration = int(period.strip('m'))*60
        return num_requests, duration
    
    def allow_request(self, request, view):
        """
        Checks if the user has exceeded the maximum number of attempts.
        """
        # Get the cache key
        if self.rate is None:
            return True
        
        self.key = self.get_cache_key(request, view)
        if self.key is None:
            return True
        # Get the number of attempts(history) from cache
        self.history = self.cache.get(self.key, [])
        print(self.history)
        
        self.now = self.timer()

        while self.history and self.history[-1] <= self.now - self.duration:
            self.history.pop()

        # Get the maximum number of attempts allowed
        max_attempts = getattr(view, "max_attempts", 3)
        print(max_attempts)
        # Check if the user has exceeded the maximum number of attempts
        if len(self.history) >= max_attempts:
            return self.throttle_failure()
        # Increment the number of attempts
        self.history.insert(0, self.now)
        self.cache.set(self.key, self.history, self.duration)
        return True


class AnonymousThrottle(AnonRateThrottle):
    
    def parse_rate(self, rate):  #10 request in very 20 seconds 
        if rate is None:
            return None, None
        num, period = rate.split('/')
        num_requests = int(num)
        duration = int(period.strip('m'))*60
        return num_requests, duration