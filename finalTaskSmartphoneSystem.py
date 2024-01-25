import getpass
import random
import string
from typing import List


class Contact:
    """Класс для представления контакта."""
    def __init__(self, name: str, phone_number: str):
        """
        Конструктор класса контакта.

        :param name: Имя контакта.
        :param phone_number: Номер телефона контакта.
        """
        self.name = name
        self.phone_number = phone_number

    def __str__(self) -> str:
        """
        Возвращает строковое представление контакта.

        :return: Строковое представление контакта.

        >>> contact = Contact("John Doe", "123-456-7890")
        >>> str(contact)
        "'John Doe: 123-456-7890'"
        """
        return f"'{self.name}: {self.phone_number}'"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление контакта.

        :return: Формальное строковое представление контакта.

        >>> contact = Contact("John Doe", "123-456-7890")
        >>> repr(contact)
        'Contact(name=John Doe, phone_number=123-456-7890)'
        """
        return f"Contact(name={self.name}, phone_number={self.phone_number})"


class ElectronicDevice:
    """Базовый класс для электронных устройств."""
    def __init__(self, brand: str, model: str, power_consumption: float):
        """
        Конструктор базового класса.

        :param brand: Бренд устройства.
        :param model: Модель устройства.
        :param power_consumption: Потребление энергии в ваттах.
        """
        self.brand = brand
        self.model = model
        self.power_consumption = power_consumption
        self.is_on = False
        self._wifi_password = None  # Переменная для хранения пароля Wi-Fi

    @property
    def wifi_password(self) -> str:
        """Геттер для атрибута _wifi_password."""
        return self._wifi_password

    @wifi_password.setter
    def wifi_password(self, password: str) -> None:
        """
        Сеттер для атрибута _wifi_password.

        :param password: Новый пароль Wi-Fi.

        >>> device = ElectronicDevice("Brand", "Model", 10.0)
        >>> device.wifi_password = "NewPassword"
        """
        self._wifi_password = password

    def input_wifi_password(self) -> str:
        """
        Метод для ввода пароля Wi-Fi с консоли без отображения ввода.

        :return: Введенный пароль Wi-Fi.

        >>> device = ElectronicDevice("Brand", "Model", 10.0)
        >>> device.input_wifi_password()  # doctest: +SKIP
        'user_input'
        """
        return getpass.getpass("Введите пароль Wi-Fi: ")

    def connect_to_wifi(self, wifi_name: str) -> bool:
        """
        Метод для подключения к Wi-Fi сети.

        :param wifi_name: Имя Wi-Fi сети.
        :return: True, если подключение успешно, False в противном случае.

        >>> device = ElectronicDevice("Brand", "Model", 10.0)
        >>> device.connect_to_wifi("MyWiFi")  # doctest: +SKIP
        """
        if self.is_on:
            if self._wifi_password is not None:
                entered_password = self.input_wifi_password()
                if entered_password != self._wifi_password:
                    print("Неверный пароль Wi-Fi. Подключение не выполнено.")
                    return False
                print(f"{self.brand} {self.model} подключается к Wi-Fi с паролем: {wifi_name}.")
            else:
                print(f"{self.brand} {self.model} подключается к Wi-Fi без пароля: {wifi_name}.")
            return True
        else:
            print("Устройство выключено. Включите его перед подключением к Wi-Fi.")
            return False

    @staticmethod
    def generate_random_password(length: int = 8) -> str:
        """
        Статический метод для генерации случайного пароля Wi-Fi.

        :param length: Длина пароля (по умолчанию 8 символов).
        :return: Случайно сгенерированный пароль Wi-Fi.

        >>> ElectronicDevice.generate_random_password(10)  # doctest: +SKIP
        'random_password'
        """
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for _ in range(length))


class SmartPhone(ElectronicDevice):
    """Дочерний класс для смартфонов."""
    def __init__(self, brand: str, model: str, power_consumption: float, apps: List[str], battery_level: float = 100.0):
        """
        Конструктор дочернего класса.

        :param brand: Бренд смартфона.
        :param model: Модель смартфона.
        :param power_consumption: Потребление энергии в ваттах.
        :param apps: Список установленных приложений.
        :param battery_level: Уровень заряда батареи (по умолчанию 100%).
        """
        super().__init__(brand, model, power_consumption)
        self.apps = apps
        self.battery_level = battery_level
        self.contacts = {}

    def turn_on(self) -> None:
        """
        Метод для включения смартфона.

        По умолчанию просто выводит сообщение о включении.

        >>> phone = SmartPhone("Samsung", "Galaxy S21", 5.0, ["Messaging", "Camera"])
        >>> phone.turn_on()
        Samsung Galaxy S21 включен.
        """
        self.is_on = True
        print(f"{self.brand} {self.model} включен.")

    def turn_off(self) -> None:
        """
        Метод для выключения смартфона.

        По умолчанию просто выводит сообщение о выключении.

        >>> phone = SmartPhone("Samsung", "Galaxy S21", 5.0, ["Messaging", "Camera"])
        >>> phone.turn_off()
        Samsung Galaxy S21 выключен.
        """
        self.is_on = False
        print(f"{self.brand} {self.model} выключен.")

    def make_call(self, contact: str) -> None:
        """
        Метод для осуществления звонка.

        :param contact: Контактный номер телефона (строка).

        >>> phone = SmartPhone(brand="Samsung", model="Galaxy S21", power_consumption=5.0, apps=["Messaging", "Camera"])
        >>> phone.turn_on()
        Samsung Galaxy S21 включен.
        >>> phone.make_call("123-456-7890")
        Samsung Galaxy S21 звонит 123-456-7890.
        """
        if self.is_on:
            print(f"{self.brand} {self.model} звонит {contact}.")
        else:
            print("Смартфон выключен. Включите его перед звонком.")

    def send_message(self, contact: str, message: str) -> None:
        """
        Метод для отправки сообщения.

        :param contact: Контактный номер телефона (строка).
        :param message: Текст сообщения (строка).

        >>> phone = SmartPhone(brand="Samsung", model="Galaxy S21", power_consumption=5.0, apps=["Messaging", "Camera"])
        >>> phone.turn_on()
        Samsung Galaxy S21 включен.
        >>> phone.send_message("123-456-7890", "Привет, как дела?")
        Samsung Galaxy S21 отправляет сообщение 123-456-7890: Привет, как дела?
        """
        if self.is_on:
            print(f"{self.brand} {self.model} отправляет сообщение {contact}: {message}")
        else:
            print("Смартфон выключен. Включите его перед отправкой сообщения.")

    def add_contact(self, name: str, phone_number: str) -> None:
        """
        Метод для добавления контакта в телефонную книгу.

        :param name: Имя контакта (строка).
        :param phone_number: Номер телефона контакта (строка).

        >>> phone = SmartPhone(brand="Samsung", model="Galaxy S21", power_consumption=5.0, apps=["Messaging", "Camera"])
        >>> phone.add_contact(name="Guido van Rossum", phone_number="650-595-XXXX")
        Контакт Guido van Rossum: 650-595-XXXX добавлен в телефонную книгу.
        >>> phone.contacts
        {'650-595-XXXX': Contact(name=Guido van Rossum, phone_number=650-595-XXXX)}

        """
        contact = Contact(name, phone_number)
        self.contacts[phone_number] = contact
        print(f"Контакт {contact.name}: {contact.phone_number} добавлен в телефонную книгу.")

    def delete_contact(self, phone_number: str) -> None:
        """
        Метод для удаления контакта из телефонной книги.

        :param phone_number: Номер телефона контакта (строка).

        >>> phone = SmartPhone(brand="Samsung", model="Galaxy S21", power_consumption=5.0, apps=["Messaging", "Camera"])
        >>> phone.add_contact(name="Guido van Rossum", phone_number="650-595-XXXX")
        Контакт Guido van Rossum: 650-595-XXXX добавлен в телефонную книгу.
        >>> phone.delete_contact("650-595-XXXX")
        Контакт Guido van Rossum удален из телефонной книги.
        >>> phone.contacts
        {}
        """
        if phone_number in self.contacts:
            deleted_contact = self.contacts.pop(phone_number)
            print(f"Контакт {deleted_contact.name} удален из телефонной книги.")
        else:
            print(f"Контакт с номером {phone_number} не найден.")

    def update_contact_name(self, phone_number: str, new_name: str) -> None:
        """
        Метод для изменения имени контакта в телефонной книге.

        :param phone_number: Номер телефона контакта (строка).
        :param new_name: Новое имя контакта (строка).
        """
        if phone_number in self.contacts:
            self.contacts[phone_number].name = new_name
            print(f"Имя контакта с номером {phone_number} изменено на {new_name}.")
        else:
            print(f"Контакт с номером {phone_number} не найден.")

    def update_contact_number(self, old_number: str, new_number: str) -> None:
        """
        Метод для изменения номера контакта в телефонной книге.

        :param old_number: Текущий номер телефона контакта (строка).
        :param new_number: Новый номер телефона контакта (строка).
        """
        if old_number in self.contacts:
            contact = self.contacts.pop(old_number)
            contact.phone_number = new_number
            self.contacts[new_number] = contact
            print(f"Номер контакта {contact.name} изменен на {new_number}.")
        else:
            print(f"Контакт с номером {old_number} не найден.")


if __name__ == "__main__":
    phone = SmartPhone(brand="Samsung", model="Galaxy S21", power_consumption=5.0, apps=["Messaging", "Camera"])

    print(phone)
    phone.turn_on()
    phone.make_call("84(3678)712-00-97")
    phone.send_message("76(62)353-86-52", "Hi! How'r u doing?")
    phone.connect_to_wifi("MyHomeWiFi")
    phone.turn_off()

    # Работа с контактами
    phone.add_contact(name="Guido van Rossum", phone_number="650-595-XXXX")
    phone.add_contact(name="Alice Smith", phone_number="0(594)070-76-85")
    print("Телефонная книга:")
    for contact in phone.contacts.values():
        print(contact)

    phone.update_contact_name(phone_number="650-595-XXXX", new_name="Python Developer")
    phone.update_contact_number(old_number="650-595-XXXX", new_number="949-788-XXXX")
    phone.delete_contact(phone_number="111-9999")

    # Работа с паролем Wi-Fi
    phone.wifi_password = "SecurePassword123"
    print(f"Текущий пароль Wi-Fi: {phone.wifi_password}")

    new_wifi_password = ElectronicDevice.generate_random_password()
    phone.wifi_password = new_wifi_password
    print(f"Новый пароль Wi-Fi: {phone.wifi_password}")
