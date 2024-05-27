workspace {
    name "Мессенджер"
    description "Система обмена сообщениями с поддержкой групповых и PtP чатов"

    # Включаем режим с иерархической системой идентификаторов
    !identifiers hierarchical

    !docs documentation
    !adrs decisions
    # Модель архитектуры
    model {

        # Настраиваем возможность создания вложенных групп
        properties { 
            structurizr.groupSeparator "/"
        }

        # Описание компонент модели
        user = person "Пользователь"
        messenger = softwareSystem "Мессенджер" {
            description "Система мгновенного обмена сообщениями"

            api_gateway = container "API Gateway" {
                description "Шлюз для маршрутизации запросов между сервисами"
                technology "Spring Cloud Gateway"
            }

            user_service = container "User Service" {
                description "Сервис для управления пользователями"
            }

            ptp_chat_service = container "PtP Chat Service" {
                description "Сервис для управления персональными чатами"
            }

            group_chat_service = container "Group Chat Service" {
                description "Сервис для управления групповыми чатами"
            }

            group "Слой данных" {
                user_database = container "User Database" {
                    description "База данных пользователей"
                    technology "PostgreSQL"
                    tags "database"
                }

                chat_database = container "Chat Database" {
                    description "База данных для хранения информации о чатах и сообщениях"
                    technology "MongoDB"
                    tags "database"
                }
            }

            user_service -> user_database "Получение/обновление данных о пользователях" "TCP 5432"
            ptp_chat_service -> chat_database "Получение/обновление данных о персональных чатах и сообщениях" "TCP 27017"
            group_chat_service -> chat_database "Получение/обновление данных о групповых чатах и сообщениях" "TCP 27017"

            api_gateway -> user_service "Маршрутизация запросов к User Service" "HTTP"
            api_gateway -> ptp_chat_service "Маршрутизация запросов к PtP Chat Service" "HTTP"
            api_gateway -> group_chat_service "Маршрутизация запросов к Group Chat Service" "HTTP"

            user -> api_gateway "Регистрация/поиск пользователей, управление чатами и сообщениями" "REST HTTP"
        }

        deploymentEnvironment "Production" {
            deploymentNode "API Gateway Server" {
                containerInstance messenger.api_gateway
            }

            deploymentNode "User Server" {
                containerInstance messenger.user_service
            }

            deploymentNode "Chat Server" {
                containerInstance messenger.ptp_chat_service
                containerInstance messenger.group_chat_service
            }

            deploymentNode "databases" {
                deploymentNode "User Database Server" {
                    containerInstance messenger.user_database
                }

                deploymentNode "Chat Database Server" {
                    containerInstance messenger.chat_database
                }
            }
        }
    }

    views {
        themes default

        properties { 
            structurizr.tooltips true
        }

        !script groovy {
            workspace.views.createDefaultViews()
            workspace.views.views.findAll { it instanceof com.structurizr.view.ModelView }.each { it.enableAutomaticLayout() }
        }

        dynamic messenger "UC01" "Создание нового пользователя" {
            autoLayout
            user -> messenger.api_gateway "Создать нового пользователя (POST /user)"
            messenger.api_gateway -> messenger.user_service "Создать нового пользователя (POST /user)"
            messenger.user_service -> messenger.user_database "Сохранить данные о пользователе"
        }

        dynamic messenger "UC02" "Поиск пользователя по логину" {
            autoLayout
            user -> messenger.api_gateway "Поиск пользователя (GET /users/login)"
            messenger.api_gateway -> messenger.user_service "Поиск пользователя (GET /users/login)"
        }

        dynamic messenger "UC03" "Поиск пользователя по маске имени и фамилии" {
            autoLayout
            user -> messenger.api_gateway "Поиск пользователя (GET /users/name)"
            messenger.api_gateway -> messenger.user_service "Поиск пользователя (GET /users/name)"
        }

        dynamic messenger "UC04" "Создание группового чата" {
            autoLayout
            user -> messenger.api_gateway "Создать групповой чат (POST /chat/group)"
            messenger.api_gateway -> messenger.group_chat_service "Создать групповой чат (POST /chat/group)"
        }

        dynamic messenger "UC05" "Добавление пользователя в групповой чат" {
            autoLayout
            user -> messenger.api_gateway "Добавить пользователя в групповой чат (POST /chat/group/add)"
            messenger.api_gateway -> messenger.group_chat_service "Добавить пользователя в групповой чат (POST /chat/group/add)"
        }

        dynamic messenger "UC06" "Добавление сообщения в групповой чат" {
            autoLayout
            user -> messenger.api_gateway "Добавить сообщение (POST /chat/group/message)"
            messenger.api_gateway -> messenger.group_chat_service "Добавить сообщение (POST /chat/group/message)"
        }

        dynamic messenger "UC07" "Загрузка сообщений группового чата" {
            autoLayout
            user -> messenger.api_gateway "Загрузить сообщения (GET /chat/group/messages)"
            messenger.api_gateway -> messenger.group_chat_service "Загрузить сообщения (GET /chat/group/messages)"
        }

        dynamic messenger "UC08" "Отправка PtP сообщения пользователю" {
            autoLayout
            user -> messenger.api_gateway "Отправить PtP сообщение (POST /chat/ptp)"
            messenger.api_gateway -> messenger.ptp_chat_service "Отправить PtP сообщение (POST /chat/ptp)"
        }

        dynamic messenger "UC09" "Получение PtP списка сообщений для пользователя" {
            autoLayout
            user -> messenger.api_gateway "Получить PtP сообщения (GET /chat/ptp/messages)"
            messenger.api_gateway -> messenger.ptp_chat_service "Получить PtP сообщения (GET /chat/ptp/messages)"
        }

        styles {
            element "database" {
                shape cylinder
            }
        }
    }
}
