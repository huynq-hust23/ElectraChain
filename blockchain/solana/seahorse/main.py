# Built with Seahorse v0.2.0

from seahorse.prelude import *

# This is your program's public key and it will update
# automatically when you build the project.
declare_id('E5cqMdTssF6ANT3Yr36KRMeHJ9h2LdWFFyhPe5HR7ddZ')

class Sha256Value:
    c1: u64
    c2: u64
    c3: u64
    c4: u64

class Voter(Account):
    owner: Pubkey # 32 bytes
    cccd_sha256: Sha256Value
    vote_who: Pubkey # 32 bytes
    voted: bool # 8 bytes

class Candidate(Account):
    # owner: Pubkey # 32 bytes
    num_votes: u64

@instruction
def init_voter(payer: Signer, owner: Signer, voter: Empty[Voter], c1: u64, c2: u64, c3: u64, c4: u64):
    voter = voter.init(payer = payer, seeds = [owner, 'voter'])
    voter.owner = owner.key()
    voter.cccd_sha256.c1 = c1
    voter.cccd_sha256.c2 = c2
    voter.cccd_sha256.c3 = c3
    voter.cccd_sha256.c4 = c4

@instruction
def init_candidate(payer: Signer, owner: Signer, candidate: Empty[Candidate]):
    candidate = candidate.init(payer = payer, seeds = [owner, 'candidate'])
    # candidate.owner = owner.key()
    candidate.num_votes = 0

@instruction
def vote(payer: Signer, voter_signer: Signer, voter: Voter, candidate: Candidate):
    assert not voter.voted, "Voter has already voted"
    assert voter_signer.key() == voter.owner, "Voter is not the owner"
    candidate.num_votes += 1
    voter.voted = True
    voter.vote_who = candidate.key()