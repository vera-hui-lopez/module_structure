import torch

__all__ = ['TensorCalculator']


class TensorCalculator:
    @staticmethod
    def tensor_zeros(dim_x: int, dim_y: int, dim_z: int) -> torch.Tensor:
        """
        Creates a tensor of zeros with 3 dimensions
        :param dim_x: length of dimension x
        :param dim_y: length of dimension y
        :param dim_z:length of dimension z
        :return: torch.Tensor with he dimensions specified
        """
        return torch.zeros(dim_x, dim_y, dim_z)

    @staticmethod
    def tensor_ones(dim_x: int, dim_y: int, dim_z: int) -> torch.Tensor:
        """
        Creates a tensor of ones with 3 dimensions
        :param dim_x: length of dimension x
        :param dim_y: length of dimension y
        :param dim_z:length of dimension z
        :return: torch.Tensor with he dimensions specified
        """
        return torch.ones(dim_x, dim_y, dim_z)

    @staticmethod
    def tensor_rand(dim_x: int, dim_y: int, dim_z: int) -> torch.Tensor:
        """
        Creates a tensor of random numbers from [0,1] with 3 dimensions
        :param dim_x: length of dimension x
        :param dim_y: length of dimension y
        :param dim_z:length of dimension z
        :return: torch.Tensor with he dimensions specified
        """

        return torch.rand(dim_x, dim_y, dim_z)

    @staticmethod
    def tensor_sum(tensor_a: torch.Tensor, tensor_b: torch.Tensor) -> torch.Tensor:
        """
        Sums two tensors
        :param tensor_a: input the first tensor
        :param tensor_b: input the second tensor
        :return: a tensor
        """
        try:
            result=tensor_a + tensor_b
            return result
        except Exception as e:
            print("Dimensions do not match:", e)

    @staticmethod
    def tensor_mult(tensor_a: torch.Tensor, tensor_b: torch.Tensor)-> torch.Tensor:
        """
        Multiplies two tensors
        :param tensor_a: input the first tensor
        :param tensor_b: input the second tensor
        :return: a tensor
        """
        try:
            result=torch.matmul(tensor_a, tensor_b)
            return result
        except Exception as e:
            print("dimensions do not match", e)

    @staticmethod
    def tensor_normalize(tensor: torch.Tensor) -> torch.Tensor:
        """
        Normalizes the values of a tensor (0,1)
        :param tensor: Input tensor
        :return: Normalized tensor
        """
        mean = torch.mean(tensor)
        std = torch.std(tensor)
        return (tensor - mean) / std

    @staticmethod
    def tensor_average(tensor: torch.Tensor) -> torch.Tensor:
        """
        Average of a tensor
        :param tensor: Input tensor
        :return:  average
        """
        return torch.mean(tensor)

    @staticmethod
    def tensor_max(tensor: torch.Tensor) -> torch.Tensor:
        """
        Maximum value in a tensor.
        :param tensor: Input tensor
        :return: Scalar tensor representing the maximum value
        """
        return torch.max(tensor)

    @staticmethod
    def tensor_min(tensor: torch.Tensor) -> torch.Tensor:
        """
        Minimum value in a tensor.
        :param tensor: Input tensor
        :return: Scalar tensor representing the minimum value
        """
        return torch.min(tensor)

