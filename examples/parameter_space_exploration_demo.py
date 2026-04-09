"""
Parameter Space Exploration Demo
=================================
Demonstrates the PSE components for automated parameter sweeps.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

import numpy as np
from xai_components.xai_pse.range_components import PSELinspaceRange, PSEArangeRange
from xai_components.xai_pse.grid_components import PSEParameterGrid
from xai_components.xai_pse.metric_components import PSEResultCollector, PSEGlobalVariance

def main():
    print("=" * 70)
    print("TVB Parameter Space Exploration Demo")
    print("=" * 70)

    print("\n[Step 1] Defining parameter ranges...")
    
    # Create G range component
    G_range = PSELinspaceRange()
    G_range.start.value = 0.0
    G_range.stop.value = 2.0
    G_range.num_points.value = 5
    G_range.execute(None)

    # Create speed range component
    speed_range = PSEArangeRange()
    speed_range.start.value = 2.0
    speed_range.stop.value = 6.0
    speed_range.step.value = 1.0
    speed_range.execute(None)

    print("\n[Step 2] Creating parameter grid...")
    grid = PSEParameterGrid()
    grid.param1_values.value = G_range.values.value
    grid.param2_values.value = speed_range.values.value
    grid.param1_name.value = "G"
    grid.param2_name.value = "speed"
    grid.execute({})  # Pass empty dict as context
    
    combinations = grid.grid_combinations.value
    print(f"  First 3 combinations:")
    for i, combo in enumerate(combinations[:3], 1):
        print(f"    {i}. G={combo[0]:.2f}, speed={combo[1]:.2f}")

    print(f"\n[Step 3] Running {len(combinations)} simulations...")
    
    # Collect all results
    all_results = []
    for i, (g_val, speed_val) in enumerate(combinations, 1):
        # Generate mock time series
        time_points = 1000
        time_series = np.random.randn(time_points, 1, 76, 1)
        signal_strength = g_val * speed_val / 5.0
        time_series += signal_strength * np.sin(np.linspace(0, 10*np.pi, time_points))[:, None, None, None]
        
        all_results.append(time_series)
        
        if i % 5 == 0:
            print(f"  [OK] Completed {i}/{len(combinations)}")
    
    print("  [OK] All simulations complete!")

    print("\n[Step 4] Computing global variance...")
    variance_metric = PSEGlobalVariance()
    variance_metric.simulation_results.value = all_results
    variance_metric.grid_shape.value = grid.grid_shape.value
    variance_metric.execute(None)
    
    variance_matrix = variance_metric.metric_matrix.value
    print(f"  [OK] Variance matrix shape: {variance_matrix.shape}")
    print(f"  [OK] Min: {np.nanmin(variance_matrix):.4f}")
    print(f"  [OK] Max: {np.nanmax(variance_matrix):.4f}")
    print(f"  [OK] Mean: {np.nanmean(variance_matrix):.4f}")

    print("\n[Step 5] Creating visualization...")
    try:
        import matplotlib.pyplot as plt
        import seaborn as sns
        
        os.makedirs('outputs', exist_ok=True)
        
        plt.figure(figsize=(10, 8))
        sns.heatmap(
            variance_matrix,
            xticklabels=[f'{x:.1f}' for x in grid.param2_axis.value],
            yticklabels=[f'{y:.1f}' for y in grid.param1_axis.value],
            cmap='viridis',
            annot=True,
            fmt='.3f',
            cbar_kws={'label': 'Global Variance'}
        )
        plt.xlabel('Conduction Speed', fontsize=12)
        plt.ylabel('Global Coupling (G)', fontsize=12)
        plt.title('Parameter Space Exploration - Global Variance', fontsize=14, fontweight='bold')
        plt.tight_layout()
        plt.savefig('outputs/pse_demo_heatmap.png', dpi=300, bbox_inches='tight')
        print("  [OK] Heatmap saved to outputs/pse_demo_heatmap.png")
    except ImportError:
        print("  [!] Visualization skipped (install: pip install matplotlib seaborn)")
    except Exception as e:
        print(f"  [!] Visualization error: {e}")

    print("\n" + "=" * 70)
    print("[DONE] Parameter Space Exploration Demo Complete!")
    print("=" * 70)
    print(f"\nSummary:")
    print(f"  - Parameters explored: 2 (G, speed)")
    print(f"  - Grid shape: {grid.grid_shape.value}")
    print(f"  - Total simulations: {grid.total_simulations.value}")
    print(f"  - Variance range: {np.nanmin(variance_matrix):.4f} - {np.nanmax(variance_matrix):.4f}")
    if os.path.exists('outputs/pse_demo_heatmap.png'):
        print(f"  - Visualization: outputs/pse_demo_heatmap.png")
    print("=" * 70)

if __name__ == "__main__":
    main()
