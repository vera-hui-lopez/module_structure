import torch

__all__ = ['TensorCalculator']


class TensorCalculator:
    @staticmethod
    def tensor_zeros(dim_x: int, dim_y: int, dim_z: int) -> torch.Tensor:
        """
        Static method that creates a tensor of zeros with 3 dimensions
        :param dim_x: length of dimension x
        :param dim_y: length of dimension y
        :param dim_z:length of dimension z
        :return: torch.Tensor with he dimensions specified
        """
        return torch.zeros(dim_x, dim_y, dim_z)

    @staticmethod
    def tensor_ones(dim_x: int, dim_y: int, dim_z: int) -> torch.Tensor:
        """
        Static method that creates a tensor of ones with 3 dimensions
        :param dim_x: length of dimension x
        :param dim_y: length of dimension y
        :param dim_z:length of dimension z
        :return: torch.Tensor with he dimensions specified
        """
        return torch.ones(dim_x, dim_y, dim_z)

    @staticmethod
    def tensor_rand(dim_x: int, dim_y: int, dim_z: int) -> torch.Tensor:
        """
        Static method that creates a tensor of random numbers from [0,1] with 3 dimensions
        :param dim_x: length of dimension x
        :param dim_y: length of dimension y
        :param dim_z:length of dimension z
        :return: torch.Tensor with he dimensions specified
        """

        return torch.rand(dim_x, dim_y, dim_z)

