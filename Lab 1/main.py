import doctest
from datetime import datetime, timedelta
from unittest.mock import patch
from typing import Optional, Set


class User:
    def __init__(self, username: str, birthdate: datetime, location: str, phone_number: str = None):
        """
        Конструктор класса User.

        Args:
            username (str): Имя пользователя.
            birthdate (datetime): Дата рождения пользователя.
            location (str): Место жительства пользователя.
            phone_number (str, optional): Номер телефона пользователя. По умолчанию None.

        Attributes:
            username (str): Имя пользователя.
            birthdate (datetime): Дата рождения пользователя.
            location (str): Место жительства пользователя.
            phone_number (str, optional): Номер телефона пользователя.
            contacts (Contacts): Объект класса Contacts для хранения контактов пользователя.
            description (str): Описание пользователя.

        Methods:
            set_description(new_username, new_birthdate, new_location, new_phone_number):
                Обновляет информацию о пользователе на основе предоставленных параметров.
            add_contact(user):
                Добавляет пользователя в контакты текущего пользователя.
            change_username(new_username):
                Изменяет имя пользователя.
            get_age():
                Возвращает возраст пользователя на основе текущей даты и даты рождения.
            get_location():
                Возвращает строку с информацией о месте жительства пользователя.

        Example:
            >>> mat = User("Mat", datetime(1990, 1, 1), "Город X", "+123456789")
            >>> mat.get_age()  # Метод get_age возвращает возраст пользователя
            33

        """
        self.username = username
        self.birthdate = birthdate
        self.location = location
        self.phone_number = phone_number
        self.contacts = Contacts()
        self.description = ""

    def set_description(
            self,
            new_username: Optional[str] = None,
            new_birthdate: Optional[datetime] = None,
            new_location: Optional[str] = None,
            new_phone_number: Optional[str] = None,
    ) -> None:
        """
        Устанавливает описание пользователя и/или обновляет другие поля.

        Args:
            new_username (str, optional): Новое имя пользователя.
            new_birthdate (datetime, optional): Новая дата рождения пользователя.
            new_location (str, optional): Новое место жительства пользователя.
            new_phone_number (str, optional): Новый номер телефона пользователя.

        Returns:
            None

        Prints:
            Сообщение с информацией об обновлении.

        Example:
            >>> mat = User("Mat", datetime(1990, 1, 1), "Город X", "+123456789")
            >>> mat.set_description(new_location="Новый город", new_phone_number="+987654321")
            Информация о пользователе Mat обновлена:
            Имя пользователя: Mat
            Дата рождения: 1990-01-01 00:00:00
            Место жительства: Новый город
            Номер телефона: +987654321

        """
        if new_username is not None:
            self.username = new_username
        if new_birthdate is not None:
            self.birthdate = new_birthdate
        if new_location is not None:
            self.location = new_location
        if new_phone_number is not None:
            self.phone_number = new_phone_number

        print(f"Информация о пользователе {self.username} обновлена:")
        print(f"Имя пользователя: {self.username}")
        print(f"Дата рождения: {self.birthdate}")
        print(f"Место жительства: {self.location}")
        print(f"Номер телефона: {self.phone_number}")

    def add_contact(self, user: "User") -> None:
        """
        Добавляет пользователя в контакты текущего пользователя.

        Args:
            user (User): Пользователь, который будет добавлен в контакты.

        Returns:
            None

        Prints:
            Сообщение о добавлении пользователя в контакты.

        Example:
            >>> mat = User("Mat", datetime(1990, 1, 1), "Город X", "+123456789")
            >>> user1 = User("User1", datetime(1985, 5, 15), "Город Y", "+987654321")
            >>> mat.add_contact(user1)
            Контакт User1 добавлен.
            Пользователь Mat добавил User1 в контакты.

        """
        self.contacts.add_contact(user)
        print(f"Пользователь {self.username} добавил {user.username} в контакты.")

    def change_username(self, new_username: str) -> None:
        """
        Изменяет имя пользователя.

        Args:
            new_username (str): Новое имя пользователя.

        Returns:
            None

        Prints:
            Сообщение об изменении имени пользователя.

        Example:
            >>> mat = User("Mat", datetime(1990, 1, 1), "Город X", "+123456789")
            >>> mat.change_username("NewMat")
            Имя пользователя изменено с Mat на NewMat.

        """
        print(f"Имя пользователя изменено с {self.username} на {new_username}.")
        self.username = new_username

    def get_age(self) -> int:
        """
        Возвращает возраст пользователя на основе текущей даты и даты рождения.

        Returns:
            int: Возраст пользователя.

        """
        today = datetime.today()
        age = today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
        return age

    def get_location(self) -> str:
        """
        Возвращает строку с информацией о месте жительства пользователя.

        Returns:
            str: Строка с информацией о месте жительства.

        Example:
            >>> mat = User("Mat", datetime(1990, 1, 1), "Город X", "+123456789")
            >>> mat.get_location()
            'Mat живет в Город X.'

        """
        return f"{self.username} живет в {self.location}."


class Contacts:
    def __init__(self) -> None:
        """
        Конструктор класса Contacts.

        Attributes:
            contacts (Set[User]): Множество контактов.

        """
        self.contacts: Set[User] = set()

    def add_contact(self, user: 'User') -> None:
        """
        Добавляет пользователя в контакты.

        Args:
            user (User): Пользователь, который будет добавлен в контакты.

        Returns:
            None

        Prints:
            Сообщение о добавлении контакта.

        Example:
            >>> contacts = Contacts()
            >>> mat = User("Mat", datetime(1990, 1, 1), "Город X", "+123456789")
            >>> contacts.add_contact(mat)
            Контакт Mat добавлен.

        """
        self.contacts.add(user)
        print(f"Контакт {user.username} добавлен.")

    @staticmethod
    def call(caller: 'User', receiver: 'User') -> None:
        """
        Инициирует звонок между двумя пользователями.

        Args:
            caller (User): Пользователь, инициирующий звонок.
            receiver (User): Пользователь, принимающий звонок.

        Returns:
            None

        Prints:
            Сообщение о начале звонка и времени его завершения.

        Example:
            >>> contacts = Contacts()
            >>> mat = User("Mat", datetime(1990, 1, 1), "Город X", "+123456789")
            >>> contacts.add_contact(mat)
            Контакт Mat добавлен.
            >>> # Ожидаем, что в doctest не будет вывода, поэтому пишем комментарий "Expected nothing."

        """
        if caller in receiver.contacts.contacts and receiver in caller.contacts.contacts:
            print(f"{caller.username} звонит {receiver.username}.")
            call_start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # Предположим, что разговор длится 1 минуту (можно адаптировать по вашему желанию)
            call_end_time = (datetime.now() + timedelta(minutes=1)).strftime("%Y-%m-%d %H:%M:%S")
            print(f"Звонок начался в {call_start_time}. Завершится в {call_end_time}.")
        else:
            print(f"Невозможно установить связь между {caller.username} и {receiver.username}.")


class Group:
    def __init__(self, name: str, creator: User, min_age_to_join: Optional[int] = 0) -> None:
        """
        Выводит информацию о пользователе в группе по его имени.

        Args:
            name (str): Название группы.
            creator (User): Создатель группы.
            min_age_to_join (int, optional): Минимальный возраст для вступления в группу. По умолчанию 0.

        Attributes:
            name (str): Название группы.
            creator (User): Создатель группы.
            min_age_to_join (int): Минимальный возраст для вступления в группу.
            members (dict): Словарь для хранения ролей участников группы.
            messages (list): Список сообщений в группе.
            contacts (Contacts): Объект класса Contacts для хранения контактов группы.

        Methods:
            add_member(user, role="member"):
                Добавляет пользователя в группу с указанной ролью.
            promote_to_admin(promoter, user):
                Повышает пользователя до админа в группе.
            demote_to_member(creator, user):
                Понижает пользователя до обычного участника группы.
            remove_member(remover, user):
                Удаляет пользователя из группы.
            send_message(sender, text):
                Отправляет сообщение в группу от указанного пользователя.
            show_info():
                Выводит информацию о группе, ее создателе, участниках и сообщениях.
            get_user_info(username):
                Выводит информацию о пользователе в группе по его имени.

        Prints:
            Информация о пользователе в группе.

        Example:
            >>> group = Group("Team", User("Admin", datetime(1990, 1, 1), "City A"), min_age_to_join=18)
            >>> user1 = User("User1", datetime(1995, 5, 15), "City B")
            >>> group.add_member(user1)
            Пользователь User1 добавлен в группу Team как member.
            Контакт User1 добавлен.
            >>> user1.description = "Likes programming."
            >>> group.get_user_info("User1")
            Информация о пользователе User1:
            Имя: User1
            Возраст: 28 лет
            Место жительства: User1 живет в City B.
            Описание: Likes programming.

        """
        self.name: str = name
        self.creator: User = creator
        self.min_age_to_join: Optional[int] = min_age_to_join
        self.members: dict = {creator: "admin"}  # Используем словарь для хранения ролей участников
        self.messages: list = []
        self.contacts: Contacts = Contacts()

    def add_member(self, user: User, role: str = "member") -> None:
        """
        Добавляет пользователя в группу с указанной ролью.

        Args:
            user (User): Пользователь, который будет добавлен в группу.
            role (str, optional): Роль пользователя. По умолчанию "member".

        Returns:
            None

        Prints:
            Сообщение о добавлении пользователя в группу.

        Example:
            >>> group = Group("Team", User("Admin", datetime(1990, 1, 1), "City A"), min_age_to_join=18)
            >>> user1 = User("User1", datetime(1995, 5, 15), "City B")
            >>> group.add_member(user1)
            Пользователь User1 добавлен в группу Team как member.
            Контакт User1 добавлен.

        """
        user_age: int = user.get_age()
        if self.min_age_to_join is not None and user_age < self.min_age_to_join:
            print(
                f"Пользователь {user.username} не может вступить в группу {self.name}, так как его возраст меньше {self.min_age_to_join} лет.")
        elif user not in self.members:
            self.members[user]: str = role
            print(f"Пользователь {user.username} добавлен в группу {self.name} как {role}.")
            self.contacts.add_contact(user)
        else:
            print(f"Пользователь {user.username} уже состоит в группе {self.name}.")

    def promote_to_admin(self, promoter: User, user: User) -> None:
        """
        Повышает пользователя до админа в группе.

        Args:
            promoter (User): Пользователь, инициирующий повышение.
            user (User): Пользователь, которого нужно повысить.

        Returns:
            None

        Prints:
            Сообщение о повышении пользователя до админа.

        Example:
            >>> group = Group("Team", User("Admin", datetime(1990, 1, 1), "City A"), min_age_to_join=18)
            >>> user1 = User("User1", datetime(1995, 5, 15), "City B")
            >>> group.add_member(user1)
            Пользователь User1 добавлен в группу Team как member.
            Контакт User1 добавлен.
            >>> group.promote_to_admin(group.creator, user1)
            Пользователь User1 был повышен до админа в группе Team.

        """
        if user in self.members and self.members[user] == "member" and (
                promoter == self.creator or self.members.get(promoter) == "admin"):
            self.members[user]: str = "admin"
            print(f"Пользователь {user.username} был повышен до админа в группе {self.name}.")
        else:
            print(f"{promoter.username} не имеет права повысить пользователя {user.username} до админа.")

    def demote_to_member(self, creator: User, user: User) -> None:
        """
        Понижает пользователя до обычного участника группы.

        Args:
            creator (User): Создатель группы.
            user (User): Пользователь, которого нужно понизить.

        Returns:
            None

        Prints:
            Сообщение о понижении пользователя.

        Example:
            >>> group = Group("Team", User("Admin", datetime(1990, 1, 1), "City A"), min_age_to_join=18)
            >>> user1 = User("User1", datetime(1995, 5, 15), "City B")
            >>> group.add_member(user1)
            Пользователь User1 добавлен в группу Team как member.
            Контакт User1 добавлен.

            >>> group.promote_to_admin(group.creator, user1)
            Пользователь User1 был повышен до админа в группе Team.

            >>> group.demote_to_member(group.creator, user1)
            Пользователь User1 был понижен до обычного пользователя в группе Team.

            >>> group.show_info()
            Информация о группе Team:
            Создатель: Admin
            Участники:
            - Admin (admin)
            - User1 (member)
            Сообщения:
        """
        if user in self.members and self.members[user] == "admin" and creator == self.creator:
            self.members[user] = "member"
            print(f"Пользователь {user.username} был понижен до обычного пользователя в группе {self.name}.")
        else:
            print(f"{creator.username} не имеет права понизить пользователя {user.username} до обычного пользователя.")

    def remove_member(self, remover: User, user: User) -> None:
        """
        Удаляет пользователя из группы.

        Args:
            remover (User): Пользователь, удаляющий другого пользователя.
            user (User): Пользователь, которого нужно удалить из группы.

        Returns:
            None

        Prints:
            Сообщение об удалении пользователя из группы.

        """
        if user in self.members:
            if remover == self.creator:
                # Создатель группы имеет право удалить любого пользователя
                del self.members[user]
                print(
                    f"Пользователь {user.username} удален из группы {self.name} (удалено создателем {remover.username}).")
            elif self.members[remover] == "admin" and self.members[user] != "admin":
                # Админ может удалить обычного пользователя
                del self.members[user]
                print(
                    f"Пользователь {user.username} удален из группы {self.name} (удалено админом {remover.username}).")
            else:
                print(f"{remover.username} не имеет права удалить пользователя {user.username}.")
        else:
            print(f"Пользователь {user.username} не найден в группе {self.name}.")

    def send_message(self, sender: User, text: str) -> None:
        """
        Отправляет сообщение в группу от указанного пользователя.

        Args:
            sender (User): Пользователь, отправляющий сообщение.
            text (str): Текст сообщения.

        Returns:
            None

        Prints:
            Сообщение о отправке сообщения в группу.

        Example:
            >>> group = Group("Team", User("Admin", datetime(1990, 1, 1), "City A"), min_age_to_join=18)
            >>> user1 = User("User1", datetime(1995, 5, 15), "City B")
            >>> group.add_member(user1)
            Пользователь User1 добавлен в группу Team как member.
            Контакт User1 добавлен.

            >>> group.remove_member(group.creator, user1)
            Пользователь User1 удален из группы Team (удалено создателем Admin).

            >>> group.show_info()
            Информация о группе Team:
            Создатель: Admin
            Участники:
            - Admin (admin)
            Сообщения:
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if sender in self.members and self.members[sender] != "banned":
            message = f"{sender.username} ({timestamp}): {text}"
            self.messages.append(message)
            print(f"{sender.username} отправил сообщение в группе {self.name}: {text}")
        else:
            print(f"{sender.username} не может отправить сообщение в группе {self.name}.")

    def show_info(self) -> None:
        """
        Выводит информацию о группе, ее создателе, участниках и сообщениях.

        Returns:
            None

        Prints:
            Информация о группе, создателе, участниках и сообщениях.

        Example:
            >>> group = Group("Team", User("Admin", datetime(1990, 1, 1), "City A"), min_age_to_join=18)
            >>> user1 = User("User1", datetime(1995, 5, 15), "City B")
            >>> user2 = User("User2", datetime(1992, 8, 20), "City C")
            >>> group.add_member(user1)
            Пользователь User1 добавлен в группу Team как member.
            Контакт User1 добавлен.

            >>> group.add_member(user2, role="admin")
            Пользователь User2 добавлен в группу Team как admin.
            Контакт User2 добавлен.

            >>> with patch('main.datetime') as mock_datetime:
            ...     mock_datetime.now.side_effect = [
            ...         datetime(2023, 12, 3, 0, 40, 58),
            ...     ]
            ...     group.send_message(user1, "Привет, как дела?")
            User1 отправил сообщение в группе Team: Привет, как дела?

            >>> group.show_info()
            Информация о группе Team:
            Создатель: Admin
            Участники:
            - Admin (admin)
            - User1 (member)
            - User2 (admin)
            Сообщения:
            User1 (2023-12-03 00:40:58): Привет, как дела?

        """
        print(f"Информация о группе {self.name}:")
        print(f"Создатель: {self.creator.username}")
        print("Участники:")
        for member, role in self.members.items():
            print(f"- {member.username} ({role})")
        print("Сообщения:")
        for message in self.messages:
            print(message)

    def get_user_info(self, username: str) -> None:
        """
        Выводит информацию о пользователе в группе по его имени.

        Args:
            username (str): Имя пользователя, информацию о котором нужно вывести.

        Returns:
            None

        Prints:
            Информация о пользователе в группе.

        Example:
            >>> group = Group("Team", User("Admin", datetime(1990, 1, 1), "City A"), min_age_to_join=18)
            >>> user1 = User("User1", datetime(1995, 5, 15), "City B")
            >>> group.add_member(user1)
            Пользователь User1 добавлен в группу Team как member.
            Контакт User1 добавлен.

            >>> user1.set_description(new_phone_number="+123456789")
            Информация о пользователе User1 обновлена:
            Имя пользователя: User1
            Дата рождения: 1995-05-15 00:00:00
            Место жительства: City B
            Номер телефона: +123456789

            >>> group.get_user_info("User1")
            Информация о пользователе User1:
            Имя: User1
            Возраст: 28 лет
            Место жительства: User1 живет в City B.
            Описание: Пользователь не оставил информации о себе

            >>> group.get_user_info("User2")
            Пользователь User2 не найден в группе Team.
        """
        for user in self.members:
            if user.username == username:
                print(f"Информация о пользователе {username}:")
                print(f"Имя: {user.username}")
                print(f"Возраст: {user.get_age()} лет")
                print(f"Место жительства: {user.get_location()}")
                if user.description:
                    print(f"Описание: {user.description}")
                else:
                    print("Описание: Пользователь не оставил информации о себе")
                return
        print(f"Пользователь {username} не найден в группе {self.name}.")


if __name__ == "__main__":
    # with open('tests.txt', 'r', encoding='utf-8') as file:
    #     input_code = file.read()
    #
    # exec(input_code)
    """
    Можно раскомментировать несколько строк выше, при этом заменить >>> в программе на другие символы, например, на ***,
    чтобы тесты не запускались автоматически, а читался код с тестами, задаваемыми через tests.txt
    *строка 'print()' ниже нужна для того, чтобы заполнить модуль 'if __name__ == "__main__":', когда строки выше закомментированы
    """
    doctest.testmod()
