import numpy as np
from sklearn.decomposition import PCA
from scipy.optimize import minimize

class TASD:
    """
    Toroidal-Attractor Signal Dynamics (TASD) framework.
    Implements the original Ψ_universe attractor equation.
    """
    def __init__(self, dim=216, gamma=0.05, hurst=0.8, variance=0.2, omega=0.1*2*np.pi):
        self.dim = dim
        self.gamma = gamma
        self.hurst = hurst
        self.variance = variance
        self.omega = omega
        self.a_i = np.random.uniform(0.5, 1.5, dim)
        self.pca = PCA(n_components=3)  # latent-space reduction

    def _kernel(self, t, features_scaled):
        """Core Ψ_universe attractor equation"""
        oscillatory = np.cos(self.omega * t) + 1j * np.sin(self.omega * t)
        dissipative = np.exp(-self.gamma * t)
        turbulence = np.random.normal(0, self.variance * t**self.hurst, self.dim)
        
        psi = (self.a_i * np.real(oscillatory * dissipative) * 
               features_scaled + turbulence)
        return psi

    def evolve(self, features, t=0.0):
        """
        Evolve input features through the attractor.
        features: numpy array of shape (n_samples, n_features)
        Returns stabilized output (PCA-reduced)
        """
        features = np.asarray(features)
        if features.ndim == 1:
            features = features.reshape(1, -1)
        
        psi = self._kernel(t, features)
        psi_reduced = self.pca.fit_transform(psi)
        return psi_reduced

    def optimize_gamma(self, features, target_stability=0.001):
        """Simple optimizer to tune gamma for stability"""
        def loss(g):
            self.gamma = g
            out = self.evolve(features, t=5.0)
            return np.std(out)
        
        result = minimize(loss, x0=self.gamma, bounds=[(0.001, 0.5)])
        self.gamma = result.x[0]
        return self.gamma

# Example usage (uncomment to test)
# if __name__ == "__main__":
#     tasd = TASD(dim=216, gamma=0.05, hurst=0.8)
#     X = np.random.uniform(2.0, 3.0, size=(500, 12))
#     output = tasd.evolve(X, t=5.0)
#     print("Output shape:", output.shape)
#     print("Stabilized range:", output.min(), "—", output.max())
