# Channel Capacity

**Summary**: The maximum rate at which information can be reliably transmitted over a communication channel — Shannon's fundamental limit on communication.

**Sources**: A Mathematical Theory of Communication.pdf

**Last updated**: 2026-05-11

---

## Definition

For a discrete noiseless channel, the **capacity** C is:

C = lim (log N(T)) / T as T → ∞

where N(T) is the number of allowed signals of duration T. In the simplest case (e.g., teletype with 32 symbols transmitted at n symbols/second), C = 5n bits per second (source: A Mathematical Theory of Communication.pdf).

For a noisy channel, Shannon's **noisy channel coding theorem** states that reliable communication is possible at any rate R < C, and impossible at any rate R > C. The surprising implication: noise does not destroy the ability to communicate — it only limits the rate. With sufficiently clever encoding, error can be made arbitrarily small (source: A Mathematical Theory of Communication.pdf).

## Computing capacity

For channels with constraints on allowed symbol sequences, Shannon models the constraints as a finite-state machine (a directed graph where states represent allowed contexts and edges represent allowed symbols). The capacity is then:

C = log W

where W is the largest real root of a characteristic equation determined by the symbol durations and the constraint graph. Shannon works out the telegraph as an explicit example, computing C ≈ 0.539 per unit time (source: A Mathematical Theory of Communication.pdf).

## Significance

Channel capacity is the bridge between [[information-entropy]] (how much information a source produces) and engineering practice (how fast a channel can carry it). If the source entropy exceeds the channel capacity, some information must be lost; if it is below capacity, reliable transmission is possible. This fundamental relationship guides the design of every communication system, from modems to fiber optics.

## Related pages

- [[information-entropy]]
- [[information-theory]]
- [[shannon-1948]]
