from collections import Counter

class Card:
  ranks = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7":7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

  def __init__(self, rank):
    self.rank = rank
    self.value = Card.ranks[rank]

  def __str__(self):
    return f"Rank={self.rank}, Value={self.value}"


class Hand:
  joker_rule = False
  types = {"High card": 1, "One pair": 2, "Two pair": 3, "Three of a kind": 4, "Full house": 5, "Four of a kind": 6, "Five of a kind": 7}
  reversed_types = dict(zip(types.values(), types.keys()))
  def __init__(self, cards: Card, bid: int):
    self.cards = cards
    self.bid = bid
    self.ranks = [card.rank for card in self.cards]
    self.values = [card.value for card in self.cards]
    self._type = None

  @property
  def type(self):
    if self._type is not None:
      return self._type

    if Hand.joker_rule and "J" in self.ranks:
      self.ranks = self.convert_jokers()

    unique = len(set(self.ranks))

    match unique:
      case 1:
        self._type = Hand.types["Five of a kind"]
      case 2:
        counter = Counter(self.ranks)
        max_count = max(counter.values())
        # This will either be 3 or 4
        if max_count == 4:
          self._type = Hand.types["Four of a kind"]
        elif max_count == 3:
          self._type = Hand.types["Full house"]
      case 3:
        counter = Counter(self.ranks)
        max_count = max(counter.values())
        # This will either be 2 or 3
        if max_count == 3:
          self._type = Hand.types["Three of a kind"]
        elif max_count == 2:
          self._type = Hand.types["Two pair"]
      case 4:
        self._type = Hand.types["One pair"]
      case 5:
        self._type = Hand.types["High card"]


    return self._type

  def convert_jokers(self):
      counter = Counter([rank for rank in self.ranks if rank != "J"])
      values = list(set(counter.values()))
      rank = None
      # This means every card was unique
      # and we need to find highest ranking card to promote
      if len(values) == 1 and values[0] == 1:
        max_value = -1
        for item in counter:
          if Card.ranks[item] > max_value:
            max_value = Card.ranks[item]
            rank = item

      elif len(values) == 0: # if all the cards are J's
        rank = 'A'
      else:
        # Get the most numerous rank
        rank = max(counter, key=counter.get)

      # Replace all J's with the most numerous rank to create a better hand
      return [rank if r == "J" else r for r in self.ranks]

  def __lt__(self, other):
      if self.type < other.type:
        return True

      # If the cards are equal hands, rank by highest card in order
      if self.type == other.type:

        for i in range(0, 5):
          if self.values[i] < other.values[i]:
            return True
          if self.values[i] > other.values[i]:
            return False

      return False

  def __str__(self):
    return f"Hand={''.join(self.ranks)}, Type={Hand.reversed_types[self.type]}({self.type}), Bid={self.bid}"

  @staticmethod
  def from_string(line):
    hand, bid = line.split()
    cards = []
    for char in hand:
      cards.append(Card(rank=char))

    return Hand(cards=cards, bid=int(bid))


def solve(joker_rule):
  Hand.joker_rule = joker_rule
  if joker_rule:
    Card.ranks["J"] = 1

  hands = []
  for line in open("input.txt"):
    hand = Hand.from_string(line)
    hands.append(hand)

  sum = 0
  for index, hand in enumerate(sorted(hands)):
    sum += hand.bid * (index + 1)

  print(sum)

solve(joker_rule=False)
solve(joker_rule=True)
