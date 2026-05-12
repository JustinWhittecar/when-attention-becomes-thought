# Von Neumann architecture

**Summary**: The design pattern, set out in John von Neumann's 1945 *First Draft of a Report on the EDVAC*, in which a single shared memory holds both instructions and data and a control unit fetches, decodes, and executes one instruction at a time -- the canonical organisation of essentially every general-purpose computer built since.

**Sources**: The Origins of Digital Computers - Unknown.pdf

**Last updated**: 2026-05-12

---

## The five organs

Von Neumann's *First Draft*, written in 1945 and circulated in unfinished form by Herman Goldstine of the Moore School (the version reprinted as Chapter 8.1 of Randell's anthology), decomposes the computer into five functional organs (source: The Origins of Digital Computers - Unknown.pdf):

1. **Central arithmetic unit (CA)** -- performs addition, subtraction, multiplication, division, and the elementary logical operations on numbers held in fast registers.
2. **Central control (CC)** -- fetches instructions from memory, decodes them, and signals the other organs to carry them out.
3. **Memory (M)** -- a single, large, fast, electronic store holding both numbers (data) and orders (instructions), uniformly addressable.
4. **Input organ (I)** -- moves information from the outside world into M.
5. **Output organ (O)** -- moves information from M back to the outside world.

The arithmetic unit and control are together the [[analytical-engine|"Mill" of the Analytical Engine]]; memory is its "Store"; the input and output organs are its card readers and printers. The decisive innovation is the *unification of code and data* in a single memory, and the consequent fetch-decode-execute cycle in the control unit. (source: The Origins of Digital Computers - Unknown.pdf)

## The fetch-decode-execute cycle

The control unit maintains a program counter that holds the address of the next instruction in M. On each step it:

1. Fetches the instruction at that address.
2. Decodes its operation code and operand fields.
3. Executes it -- which may read or write a memory cell, perform an arithmetic operation, transfer to an I/O device, or change the program counter itself.
4. Increments the program counter (unless the instruction was a branch).

Conditional branching is achieved by an instruction that writes a new value into the program counter if some condition holds. Loops, subroutines, and recursion all reduce to this single mechanism. The architecture is sequential by default but Turing-universal in capability. (source: The Origins of Digital Computers - Unknown.pdf)

## Why this design and not another

Von Neumann's draft considered and rejected several alternatives (source: The Origins of Digital Computers - Unknown.pdf):

- **Separate code and data memories** ([[harvard-mark-i|Harvard architecture]]). The Mark I had instructions on punched paper tape and data in mechanical registers. This works, but it makes branching slow and forbids self-modifying code.
- **Plug-board programming** ([[eniac|ENIAC]]). ENIAC was programmed by physically rewiring the machine for each problem -- a process that could take days. Storing instructions in fast memory reduced this to seconds.
- **Decimal arithmetic** (Mark I, ENIAC, the Bell Labs relay machines). Von Neumann argued for binary on the grounds that binary digits map directly onto the two-state behaviour of flip-flops and relays, as Shannon had shown in [[shannon-1938]]. Binary requires fewer components and admits simpler arithmetic circuits.

The combination of binary arithmetic, electronic memory, and unified code/data storage is what defines the architecture.

## Bottlenecks and limits

Because the control unit must fetch each instruction sequentially over a single bus connecting it to memory, the rate of computation is bounded by the speed of that bus -- the so-called **von Neumann bottleneck**. Modern processors mitigate this with caches, pipelining, branch prediction, and parallel execution units, but the fundamental serial structure remains.

Specialised architectures break with von Neumann's design in various ways:

- **GPUs and TPUs** that train [[transformer-architecture|Transformers]] use thousands of arithmetic units operating in parallel on contiguous arrays, treating the program more like a fixed dataflow graph than a serial instruction stream.
- **Neuromorphic chips** model individual neurons asynchronously and discard the program counter entirely.
- **Analog computers** dispense with discrete instructions altogether.

But every CPU on which the GPU sits, every operating system that schedules the training run, every Python interpreter that builds the computational graph, is a von Neumann machine. The architecture has survived eighty years of technological change because its central abstraction -- programs are data in memory -- is the same abstraction that makes a [[universal-machine|universal machine]] universal. (source: The Origins of Digital Computers - Unknown.pdf)

## Authorship and the name

Von Neumann's name appears alone on the *First Draft*, but the underlying design grew out of months of discussion with J. Presper Eckert, John Mauchly, Herman Goldstine, and Arthur Burks at the Moore School during the construction of [[eniac|ENIAC]]. Eckert in particular had proposed the stored-program idea independently in a January 1944 memo on mercury delay lines. Goldstine circulated the *First Draft* under von Neumann's name only, which fixed the attribution. The name "von Neumann architecture" has been contested ever since on grounds of fairness to Eckert and Mauchly, but it has stuck. (source: The Origins of Digital Computers - Unknown.pdf)

## Related pages

- [[edvac]]
- [[stored-program-computer]]
- [[eniac]]
- [[manchester-baby]]
- [[edsac]]
- [[harvard-mark-i]]
- [[universal-machine]]
- [[turing-machine]]
- [[turing-1936]]
- [[analytical-engine]]
- [[shannon-1938]]
- [[boolean-algebra]]
- [[petzold-2023]]
- [[randell-1973]]
