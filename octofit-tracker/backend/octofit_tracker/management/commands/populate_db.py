from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create users
        ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel)
        captain = User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel)
        batman = User.objects.create(name='Batman', email='batman@dc.com', team=dc)
        superman = User.objects.create(name='Superman', email='superman@dc.com', team=dc)

        # Create workouts
        workout1 = Workout.objects.create(name='Cardio Blast', description='High intensity cardio', difficulty='Hard')
        workout2 = Workout.objects.create(name='Strength Training', description='Build muscle', difficulty='Medium')

        # Create activities
        Activity.objects.create(user=ironman, type='Running', duration=30, calories=300, date='2025-11-01')
        Activity.objects.create(user=batman, type='Cycling', duration=45, calories=400, date='2025-11-02')
        Activity.objects.create(user=superman, type='Swimming', duration=60, calories=500, date='2025-11-03')
        Activity.objects.create(user=captain, type='Yoga', duration=20, calories=100, date='2025-11-04')

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=700)
        Leaderboard.objects.create(team=dc, points=900)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
