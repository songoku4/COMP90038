import matplotlib.pyplot as plt

# EXPERIMENT 1 DATA
L_exp1 = [0.1, 0.2, 0.5, 0.8, 1.0]
arr_exp1 = [18616.52, 45938.28, 74441.20, 114566.56, 138809.92]
heap_exp1 = [87859.76, 142679.74, 303344.02, 542701.72, 531093.34]

plt.figure(figsize=(8, 5))
plt.plot(L_exp1, arr_exp1, marker='o', label='Competitor Array', linewidth=2)
plt.plot(L_exp1, heap_exp1, marker='o', label='Max-Heap', linewidth=2)
plt.title('Exp 1: Time v.s. Length of push-only Sequence')
plt.xlabel('Length L (Millions)')
plt.ylabel('Total Running Time (microseconds)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('Exp1_Graph.pdf')
plt.close()


# EXPERIMENT 2 DATA
pct_exp2 = [0.1, 0.5, 1.0, 5.0, 10.0]
arr_exp2 = [205355.84, 151179.56, 143606.56, 170137.24, 181388.74]
heap_exp2 = [608832.36, 553381.38, 592267.56, 582791.60, 552508.30]

plt.figure(figsize=(8, 5))
plt.plot(pct_exp2, arr_exp2, marker='o', label='Competitor Array', linewidth=2)
plt.plot(pct_exp2, heap_exp2, marker='o', label='Max-Heap', linewidth=2)
plt.title('Exp 2: Time v.s. getTop Percentage')
plt.xlabel('% getTop Operations')
plt.ylabel('Total Running Time (microseconds)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('Exp2_Graph.pdf')
plt.close()

# EXPERIMENT 3 DATA
pct_exp3 = [0.1, 0.5, 1.0, 5.0, 10.0]
arr_exp3 = [21631698.78, 116571772.36, 199970913.00, 1367707777.12, 1660426767.84]
heap_exp3 = [519605.82, 589543.58, 583833.38, 1150365.62, 1255206.14]

plt.figure(figsize=(8, 5))
plt.plot(pct_exp3, arr_exp3, marker='o', label='Competitor Array', linewidth=2)
plt.plot(pct_exp3, heap_exp3, marker='o', label='Max-Heap', linewidth=2)
plt.title('Exp 3: Time v.s. pop Percentage')
plt.xlabel('% pop Operations')
plt.ylabel('Total Running Time (microseconds)')
#Logarithmic scale for the Y-axis so the Heap line doesn't vanish
plt.yscale('log') 
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('Exp3_Graph.pdf')
plt.close()

# EXPERIMENT 4 DATA
L_exp4 = [0.1, 0.2, 0.5, 0.8, 1.0]
heapify_exp4 = [52613.10, 92282.78, 186433.40, 382177.74, 396855.62]
push_exp4 = [82420.44, 126808.22, 296922.04, 503807.30, 555958.98]

plt.figure(figsize=(8, 5))
plt.plot(L_exp4, heapify_exp4, marker='o', label='Method 1: heapify(σ)', linewidth=2)
plt.plot(L_exp4, push_exp4, marker='o', label='Method 2: push-one-by-one(σ)', linewidth=2)
plt.title('Exp 4: Heapify v.s. Push-One-by-One')
plt.xlabel('Length L (Millions)')
plt.ylabel('Total Running Time (microseconds)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('Exp4_Graph.pdf')
plt.close()

