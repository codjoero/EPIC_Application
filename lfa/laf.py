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

    def edit_score(self, email, day, new_score):
        """
        Modifies scores

        Args:
            email(str): Uniquely identify a user
            day(str): Day to assign a score
            score(int): Score for a given day
        """
        for user in self.users:
            if user["email"] == email:
                user["scores"][day] = new_score
                break
        return 1

    def get_scores(self, lfa):
        """
        Retrievs a list of all scores for the LFA's candidates

        Args:
            lfa(str): Identifies an lfa
        """
        scores = []
        for user in self.users:
            if user["lfa"] == lfa:
                scores.append({
                    "email": user["email"],
                    "scores": user["scores"]
                })
        return scores

    def get_all_scores(self):
        """
        Gets all scores for all bootcampers
        """
        scores = []
        for user in self.users:
            if user["type"] == "bootcamper":
                scores.append({
                    "email": user["email"],
                    "scores": user["scores"]
                })
        return scores

    def get_bootcamper_score(self, email):
        """
        Gets scores for a particular bootcamper

        Args:
            email(str): Bootcamper identifier
        """
        scores = {}
        for user in self.users:
            if user["email"] == email:
                scores = user["scores"]
                break
        return scores
