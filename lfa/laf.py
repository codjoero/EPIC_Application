class Score:
    def __init__(self, day, score):
        self.day = day
        self.score = score
        self.users = [
            {
                "email": "b@gmail.com",
                "lfa": "Barna",
                "scores": {
                    "MON": 3,
                    "TUE": 2
                }
            }
        ]

    def add_score(self, email, day, score):
        """
        Adds a score 

        Args:
            email(str): Uniquely identify a user
            day(str): Day to assign a score
            score(int): Score for a given day
        """
        for user in self.users:
            if user["email"] == email:
                user["scores"].update({day: score})
                break
        return 1

    
