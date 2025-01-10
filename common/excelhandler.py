import pandas as pd


class ExcelHandler:
    """
    Excel文件读取类

    该类的目的是提供一个简单的接口来读取Excel文件中的数据。
    它通过构造函数接收一个文件路径，并提供一个方法来读取该Excel文件。
    """

    def __init__(self, file_path):
        """
        初始化ExcelReader实例

        参数:
        file_path (str): 要读取的Excel文件的路径
        """
        self.file_path = file_path

    def read_excel(self):
        """
        从Excel文件读取数据

        该方法使用pandas库从指定路径读取Excel文件，并将数据内容返回为DataFrame对象。

        返回:
        DataFrame: 包含Excel文件数据的pandas DataFrame对象
        """
        df = pd.read_excel(self.file_path)
        return df


if __name__ == "__main__":
    filepath = r"D:\CODE\AUTOMATED_UI_QA\test_case_data\项目告警类型.xlsx"

    df = ExcelHandler(filepath).read_excel()
    print(df.iloc(1))
    # print(df.shape)
    # print(df.columns)
    # print(df.index)
    # print(df.head())
    # print(df.tail())
    # print(df.info)
    print(df.loc[1])
