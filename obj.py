class keyPair:
    def __init__(self, public, private):
        self.public_ = public
        self.private_ = private
        self.n = self.public_ * self.private_
        self.phiN = (self.public_ - 1) * (self.private_ - 1)

    def public(self):
        # public key should always be available
        return self.public

    def private(self, accessCode):
        # need to authenticate that the user can access this information
        pass


    def __repr__(self):
        return "Public: {}\nPrivate: {}\nN: {}\nphiN: {}".format(
            self.public_, self.private_, self.n, self.phiN
        )

    def __str__(self):
        return "Public: {}\nPrivate: {}\nN: {}\nphiN: {}".format(
            self.public_, self.private_, self.n, self.phiN
        )

class euclidMap:
    def __init__(self,rem,multiplier):
        self.remainder = rem
        self.multiplier = multiplier

